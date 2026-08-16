from django.shortcuts import render,redirect
from contact.forms import ContactMessageForm
from site_config.models import SiteSetting
from django.http import JsonResponse




# Create your views here.



def contact_us(request):
    if request.method == 'POST':

        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()

            return JsonResponse({
                'type': 'success',
                'message': 'پیام شما با موفقیت ارسال شد.'
            })

        return JsonResponse({
            'type': 'error',
            'message': 'لطفاً اطلاعات وارد شده را بررسی کنید.'
        }, status=400)

    form = ContactMessageForm()

    site_info = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_info': site_info,
        'form': form,
    }
    return render(request, 'contact/contact_us.html',context)