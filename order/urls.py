from django.urls import path
from . import views

urlpatterns = [
    path('add-to-order/', views.add_product_to_order, name='add_product_to_order'),

    path('checkout/', views.checkout, name='checkout'),

    path('payment/', views.payment, name='payment'),

    path('payment/success/<int:order_id>/', views.payment_success, name='payment_success'),

    path('my-orders/', views.my_orders, name='my_orders'),

    path('my-orders/<int:order_id>/', views.order_detail, name='order_detail'),

]