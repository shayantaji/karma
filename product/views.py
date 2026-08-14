from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from product.models import Product, ProductCategory, ProductBrand
from django.db.models import Count, Q, F, ExpressionWrapper, FloatField,Min,Max

from site_config.models import SiteBanner


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
        #filter_category
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

        #Brand
        brand = self.request.GET.get('brand')
        if brand:
            queryset = queryset.filter(brand__slug=brand)

        #filter_price
        queryset = queryset.annotate(
            calculated_final_price=ExpressionWrapper(
                F('price') - (F('price') * F('discount_percent') / 100),
                output_field=FloatField()
            )
        )
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        price_queryset = queryset
        if min_price:
            queryset = queryset.filter(calculated_final_price__gte=min_price)
        if max_price:
            queryset = queryset.filter(calculated_final_price__lte=max_price)
        self.price_range = price_queryset.aggregate(
            min_price=Min('calculated_final_price'),
            max_price=Max('calculated_final_price')
        )

        #sort_filter
        sort = self.request.GET.get('sort', '1')

        if sort == '2':
            queryset = queryset.order_by('-created_date')

        elif sort == '3':
            queryset=queryset.order_by('calculated_final_price')
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

        context['brands'] = ProductBrand.objects.filter(is_active=True)[:10]

        context['price_range'] = self.price_range

        query_params = self.request.GET.copy()
        query_params.pop('page', None)
        context['query_params'] = query_params.urlencode()

        context['weekly_deals'] = Product.objects.filter(is_active=True,is_deleted=False,discount_percent__gt=0
        ).select_related('category','brand').prefetch_related('images').order_by('-discount_percent')[:9]

        context['site_banner'] = SiteBanner.objects.filter(position=SiteBanner.SiteBannerPositions.PRODUCT_LIST,is_active=True).first()

        return context

class ProductSingleView(DetailView):
    template_name = 'product/product_single.html'
    model = Product
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['related_products'] = Product.objects.filter(category=self.object.category,is_active=True,is_deleted=False
        ).exclude(id=self.object.id).select_related('category','brand').prefetch_related('images')[:9]

        return context

