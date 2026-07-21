from django.shortcuts import render

# Create your views here.


def home_page(request):

    context = {}

    return  render(request,'home_page/home_page.html',context)


def header_site_component(request):
    context = {}

    return render(request,"main/header_site_component.html",context)



def footer_site_component(request):

    context = {}

    return render(request,"main/footer_site_component.html",context)



