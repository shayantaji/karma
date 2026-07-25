from django.contrib import admin
from site_config import models
# Register your models here.


class SiteSettingAdmin(admin.ModelAdmin):

    list_display = ['site_name','email']
    list_editable = ('email',)


admin.site.register(models.SiteSetting, SiteSettingAdmin)