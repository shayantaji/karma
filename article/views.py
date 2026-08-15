from django.db.models import Count, Q
from django.views.generic import TemplateView, ListView, DetailView
from article.models import Article, ArticleCategory, ArticleTag
from site_config.models import SiteBanner


# Create your views here.


class ArticleView(ListView):
    template_name = 'article/article_list.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 3

    def get_queryset(self):
        queryset = Article.objects.filter(is_active=True,is_deleted=False).select_related('category','author').prefetch_related('tags')

        category = self.request.GET.get('category')

        if category:
            queryset = queryset.filter(category__slug=category)

        tag = self.request.GET.get('tag')

        if tag:
            queryset = queryset.filter(tags__slug=tag)

        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = ArticleCategory.objects.filter(is_active=True).annotate(article_count=Count('articles'
        ,filter=Q(articles__is_active=True,articles__is_deleted=False))).order_by('-article_count')[:3]

        context['categories_sidebar'] = ArticleCategory.objects.filter(is_active=True).annotate(article_count=Count('articles'
        ,filter=Q(articles__is_active=True,articles__is_deleted=False))).order_by('-article_count')[:8]

        context['tags'] = ArticleTag.objects.filter(is_active=True)

        context['popular_articles'] = Article.objects.filter(is_active=True,is_deleted=False).order_by('-view_count')[:4]


        query_params = self.request.GET.copy()
        query_params.pop('page', None)
        context['query_params'] = query_params.urlencode()

        context['site_banner'] = SiteBanner.objects.filter(position=SiteBanner.SiteBannerPositions.ARTICLE_LIST,is_active=True).first()

        return context

class ArticleSingleView(DetailView):
    template_name = 'article/article_single.html'
    model = Article
    context_object_name = 'article'

    def get_object(self, queryset=None):
        article = super().get_object(queryset)

        article.view_count += 1
        article.save(update_fields=['view_count'])

        return article

    def get_queryset(self):

        return Article.objects.filter(is_active=True,is_deleted=False).select_related('category','author').prefetch_related('tags')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['site_banner'] = SiteBanner.objects.filter(position=SiteBanner.SiteBannerPositions.ARTICLE_DETAIL,is_active=True).first()

        context['popular_articles'] = Article.objects.filter(is_active=True, is_deleted=False).order_by('-view_count')[:4]


        context['categories_sidebar'] = ArticleCategory.objects.filter(is_active=True).annotate(article_count=Count('articles'
        ,filter=Q(articles__is_active=True,articles__is_deleted=False))).order_by('-article_count')[:8]

        context['tags'] = ArticleTag.objects.filter(is_active=True)[:10]

        return context