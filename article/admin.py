from django.contrib import admin
from article.models import Article,ArticleCategory,ArticleTag,ArticleComment




class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','is_active']
    list_editable = ['is_active']
    list_filter = ['author', 'tags']


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title','is_active']
    list_editable = ['is_active']
    list_filter = ['is_active']


class ArticleTagAdmin(admin.ModelAdmin):

    list_display = ['title','is_active']
    list_editable = ['is_active']
    list_filter = ['is_active']


class  ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ['user' ,'article']
    list_editable = ['article']


admin.site.register(Article,ArticleAdmin)
admin.site.register(ArticleTag,ArticleTagAdmin)
admin.site.register(ArticleCategory,ArticleCategoryAdmin)
admin.site.register(ArticleComment,ArticleCommentAdmin)

