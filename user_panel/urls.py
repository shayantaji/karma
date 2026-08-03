from django.urls import path
from . import  views
urlpatterns = [

        path('tracking/',views.TrackingView.as_view(),name='tracking'),

        path('change-password/',views.ChangePasswordView.as_view(),name='change_password'),


]