from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from product.models import Product, ProductCategory, ProductBrand
from django.db.models import Count, Q, F, ExpressionWrapper, FloatField


# Create your views here.


class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 9

    def get_paginate_by(self, queryset):
        per_page = self.request.GET.get('per_page')

        if per_page in ['6', '9', '12']:
            return int(per_page)

        return self.paginate_by

    def get_queryset(self):
        queryset = Product.objects.filter(
            is_active=True,
            is_deleted=False
        )

        category = self.request.GET.get('category')

        if category:
            selected_category = ProductCategory.objects.filter(
                slug=category,
                is_active=True
            ).first()

            if selected_category:
                if selected_category.parent is None:
                    child_ids = selected_category.children.filter(
                        is_active=True
                    ).values_list('id', flat=True)

                    queryset = queryset.filter(
                        Q(category=selected_category) |
                        Q(category_id__in=child_ids)
                    )
                else:
                    queryset = queryset.filter(
                        category=selected_category
                    )

        sort = self.request.GET.get('sort', '1')

        if sort == '2':
            queryset = queryset.order_by('-created_date')

        elif sort == '3':
            queryset = queryset.annotate(
                calculated_final_price=ExpressionWrapper(
                    F('price') - (
                            F('price') * F('discount_percent') / 100
                    ),
                    output_field=FloatField()
                )
            ).order_by('calculated_final_price')

        else:
            queryset = queryset.order_by('-created_date')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = ProductCategory.objects.filter(parent=None, is_active=True).prefetch_related('children')

        for category in categories:
            child_ids = category.children.filter(is_active=True).values_list('id', flat=True)
            category.product_count = Product.objects.filter(
                Q(category=category) | Q(category_id__in=child_ids),
                is_active=True,
                is_deleted=False
            ).count()
            for child in category.children.all():
                child.product_count = Product.objects.filter(
                    category=child,
                    is_active=True,
                    is_deleted=False
                ).count()

        context['categories'] = categories

        context['brands'] = ProductBrand.objects.filter(is_active=True)

        query_params = self.request.GET.copy()
        query_params.pop('page', None)
        context['query_params'] = query_params.urlencode()


        return context

class ProductSingleView(DetailView):
    template_name = 'product/product_single.html'
    model = Product
    context_object_name = "product"