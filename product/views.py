from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from product.models import Product


# Create your views here.


class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model = Product
    context_object_name = 'products'

class ProductSingleView(DetailView):
    template_name = 'product/product_single.html'
    model = Product
    context_object_name = "product"