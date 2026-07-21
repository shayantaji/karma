from django.urls import path
from . import views

urlpatterns = [


    path('', views.ArticleView.as_view(), name='article'),

    path('<slug:slug>/', views.ArticleSingleView.as_view(), name='article_single'),
]