from django.urls import path
from .views import NewsletterSubscribeView

urlpatterns = [
    path('newsletter/subscribe/', NewsletterSubscribeView.as_view(), name='newsletter_subscribe'),
]