from django.urls import path
from . import views

urlpatterns = [

    path('tracking/', views.tracking, name='tracking'),

    path('change-password/', views.ChangePasswordView.as_view(), name='change_password'),

    path('user-basket/', views.user_basket, name='user_basket_page'),

    path('remove-order-detail/', views.remove_order_detail, name='remove_order_detail_ajax'),

    path('change-order-detail/', views.change_order_detail_count, name='change_order_detail_count_ajax'),

    path('favorites/', views.UserFavoritesView.as_view(), name='user_favorites'),

    path('toggle-favorite/', views.toggle_favorite, name='toggle_favorite'),

    path('user-panel/', views.user_panel, name='user_panel'),

]