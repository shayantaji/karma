from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View
from .forms import NewsletterForm
from .models import NewsletterSubscriber


class NewsletterSubscribeView(View):
    def post(self, request):
        form = NewsletterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']

            subscriber, created = NewsletterSubscriber.objects.get_or_create(
                email=email
            )

            if created:
                message = 'با موفقیت در خبرنامه عضو شدید.'
                message_type = 'success'

            elif not subscriber.is_active:
                subscriber.is_active = True
                subscriber.save(update_fields=['is_active'])
                message = 'اشتراک شما در خبرنامه دوباره فعال شد.'
                message_type = 'success'

            else:
                message = 'این ایمیل قبلاً در خبرنامه عضو شده است.'
                message_type = 'info'

        else:
            message = 'لطفاً یک ایمیل معتبر وارد کنید.'
            message_type = 'error'

        return JsonResponse({
            'message': message,
            'type': message_type
        })