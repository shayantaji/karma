from django.contrib import admin
from user_panel.models import *

# Register your models here.


class UserFavoriteAdmin(admin.ModelAdmin):
    list_display = ['user','product']
    list_editable = ('product',)


admin.site.register(UserFavorite,UserFavoriteAdmin)