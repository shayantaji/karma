from django.contrib import admin
from site_config import models
# Register your models here.


class SiteSettingAdmin(admin.ModelAdmin):

    list_display = ['site_name','email']
    list_editable = ('email',)



class FooterKarmaGalleryListInline(admin.TabularInline):

    model = models.FooterKarmaGalleryList
    extra = 8


class FooterKarmaGalleryAdmin(admin.ModelAdmin):
    list_display = ['site']
    inlines = [FooterKarmaGalleryListInline]


class SiteBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'position']



admin.site.register(models.SiteSetting, SiteSettingAdmin)
admin.site.register(models.FooterKarmaGallery,FooterKarmaGalleryAdmin)
admin.site.register(models.SiteBanner, SiteBannerAdmin)