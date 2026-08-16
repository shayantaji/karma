from django.shortcuts import render

from product.models import Product, ProductCategory
from site_config.models import SiteSetting, FooterKarmaGallery


# Create your views here.


def home_page(request):

    weekly_deals = Product.objects.filter(is_active=True,is_deleted=False,discount_percent__gt=0
        ).select_related('category','brand').prefetch_related('images').order_by('-discount_percent')[:9]

    special_products = Product.objects.filter(is_active=True,is_deleted=False,is_special=True
    ).select_related('category','brand').prefetch_related('images')[:8]

    latest_products = Product.objects.filter(is_active=True,is_deleted=False
    ).select_related('category','brand').prefetch_related('images').order_by('-created_date')[:8]


    site_info = SiteSetting.objects.filter(is_main_setting=True).first()

    categories = ProductCategory.objects.filter(
        parent=None,
        is_active=True
    )[:5]

    context = {
        'site_info': site_info,
        'weekly_deals': weekly_deals,
        'special_products': special_products,
        'categories': categories,
        'latest_products': latest_products,
    }

    return  render(request,'home_page/home_page.html',context)


def header_site_component(request):
    site_info = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_info': site_info,
    }

    return render(request,"main/header_site_component.html",context)



def footer_site_component(request):
    footer_gallery = FooterKarmaGallery.objects.first()
    site_info = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_info': site_info,
        'footer_gallery': footer_gallery,
    }

    return render(request,"main/footer_site_component.html",context)



