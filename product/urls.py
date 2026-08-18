from django.urls import path

from . import  views


urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),

    path('<slug:slug>',views.ProductSingleView.as_view(), name='product_single'),

    path('product/<int:product_id>/comment/',views.add_product_comment,name='add_product_comment'),

    path('comments/load/<int:product_id>/',views.load_more_product_comments,name='load_more_product_comments'
),

]