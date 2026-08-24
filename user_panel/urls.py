from django.urls import path
from . import  views
urlpatterns = [

        path('tracking/',views.TrackingView.as_view(),name='tracking'),

        path('change-password/',views.ChangePasswordView.as_view(),name='change_password'),

         path('user-basket', views.user_basket, name='user_basket_page'),

         path('remove-order-detail', views.remove_order_detail, name='remove_order_detail_ajax'),

         path('change-order-detail', views.change_order_detail_count, name='change_order_detail_count_ajax'),


]