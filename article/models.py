from django.db import models
from django.urls import reverse

from account_module.models import User


class ArticleCategory(models.Model):

    title = models.CharField(max_length=200, verbose_name='عنوان')

    slug = models.SlugField(unique=True, verbose_name='اسلاگ')

    is_active = models.BooleanField(default=True, verbose_name='فعال')

    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی مقالات'

    def __str__(self):
        return self.title


class ArticleTag(models.Model):

    title = models.CharField(max_length=150)

    slug = models.SlugField(unique=True)

    is_active = models.BooleanField(default=True, verbose_name='فعال')

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def __str__(self):
        return self.title



class Article(models.Model):

    title = models.CharField(max_length=300)

    slug = models.SlugField(unique=True)

    category = models.ForeignKey(ArticleCategory,on_delete=models.PROTECT,related_name='articles')

    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    tags = models.ManyToManyField(ArticleTag,blank=True,related_name='articles')

    image = models.ImageField(upload_to='articles/',blank=True,null=True)

    short_description = models.CharField(max_length=500)

    description = models.TextField()

    view_count = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    is_deleted = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_single', args=[self.slug])