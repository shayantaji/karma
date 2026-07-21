from django.views.generic import TemplateView


from django.shortcuts import render

# Create your views here.


class ArticleView(TemplateView):
    template_name = 'article/article.html'


class ArticleSingleView(TemplateView):
    template_name = 'article/article_single.html'