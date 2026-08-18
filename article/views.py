from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import  ListView, DetailView
from article.forms import ArticleCommentForm
from article.models import Article, ArticleCategory, ArticleTag, ArticleComment
from site_config.models import SiteBanner
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string

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

        comments = self.object.comments.filter(parent__isnull=True).select_related('user').prefetch_related('replies__user')

        context['comments_count'] = comments.count()

        paginator = Paginator(comments, 10)

        context['comments'] = paginator.page(1)

        context['comments_has_next'] = paginator.num_pages > 1

        context['comment_form'] = ArticleCommentForm()

        return context


@login_required(login_url='/login/')
def add_article_comment(request, article_id):

    if request.method != 'POST':
        return JsonResponse({
            'type': 'error',
            'message': 'درخواست نامعتبر است.'
        }, status=400)

    article = get_object_or_404(Article,id=article_id,is_active=True,is_deleted=False)

    form = ArticleCommentForm(request.POST)

    if not form.is_valid():
        return JsonResponse({
            'type': 'error',
            'message': 'لطفاً متن نظر را وارد کنید.'
        }, status=400)

    comment = form.save(commit=False)
    comment.article = article
    comment.user = request.user

    parent_id = request.POST.get('parent_id')

    if parent_id:
        parent = get_object_or_404(
            ArticleComment,
            id=parent_id,
            article=article
        )

        if parent.parent_id is not None:
            return JsonResponse({
                'type': 'error',
                'message': 'امکان پاسخ به پاسخ وجود ندارد.'
            }, status=400)

        comment.parent = parent

    comment.save()

    return JsonResponse({
        'type': 'success',
        'message': 'نظر شما با موفقیت ثبت شد.',
        'comment': {
            'id': comment.id,
            'username': comment.user.get_full_name() or comment.user.username,
            'text': comment.text,
            'date': comment.created_date.strftime('%Y/%m/%d %H:%M'),
        }
    })

def load_more_comments(request, article_id):

    page = request.GET.get('page', 1)

    comments = ArticleComment.objects.filter(
        article_id=article_id,
        parent__isnull=True
    ).select_related(
        'user'
    ).prefetch_related(
        'replies__user'
    )

    paginator = Paginator(comments, 10)

    comments_page = paginator.get_page(page)

    html = render_to_string(
        'includes/comment_list/comment_list.html',
        {
            'comments': comments_page,
            'user': request.user
        },
        request=request
    )

    return JsonResponse({
        'html': html,
        'has_next': comments_page.has_next()
    })