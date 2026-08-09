from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from product.models import Product, ProductCategory, ProductBrand


# Create your views here.


class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = ProductCategory.objects.filter(parent=None,is_active=True).prefetch_related('children')

        context['brands'] = ProductBrand.objects.filter(is_active=True)

        return context


class ProductSingleView(DetailView):
    template_name = 'product/product_single.html'
    model = Product
    context_object_name = "product"