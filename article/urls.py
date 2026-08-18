from django.urls import path
from . import views
from .views import load_more_comments

urlpatterns = [


    path('', views.ArticleView.as_view(), name='article_list'),

    path('<slug:slug>/', views.ArticleSingleView.as_view(), name='article_single'),

    path('article/<int:article_id>/comment/',views.add_article_comment,name='add_article_comment'),

    path('comments/load/<int:article_id>/',load_more_comments,name='load_more_comments'),

]