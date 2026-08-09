from django.views.generic import TemplateView, ListView, DetailView
from article.models import Article, ArticleCategory, ArticleTag


# Create your views here.


class ArticleView(ListView):
    template_name = 'article/article_list.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ArticleCategory.objects.filter(is_active=True)[:3]
        context['tags'] = ArticleTag.objects.filter(is_active=True)
        context['popular_articles'] = Article.objects.filter(is_active=True,is_deleted=False).order_by('-view_count')[:4]
        return context

class ArticleSingleView(DetailView):
    template_name = 'article/article_single.html'
    model = Article
    context_object_name = 'article'

    def get_queryset(self):

        return Article.objects.filter(is_active=True,is_deleted=False).select_related('category','author').prefetch_related('tags')