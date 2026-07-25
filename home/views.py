from django.shortcuts import render

from site_config.models import SiteSetting


# Create your views here.


def home_page(request):
    site_info = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_info': site_info,
    }

    return  render(request,'home_page/home_page.html',context)


def header_site_component(request):
    site_info = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_info': site_info,
    }

    return render(request,"main/header_site_component.html",context)



def footer_site_component(request):

    site_info = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_info': site_info,
    }

    return render(request,"main/footer_site_component.html",context)



