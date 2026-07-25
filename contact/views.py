from django.shortcuts import render
from site_config.models import SiteSetting




# Create your views here.



def contact_us(request):

    site_info = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_info': site_info,
    }
    return render(request, 'contact/contact_us.html',context)