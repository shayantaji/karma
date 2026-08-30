

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'username',
        'phone',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )

    search_fields = (
        'username',
        'phone',
        'first_name',
        'last_name',
        'email',
    )

    fieldsets = UserAdmin.fieldsets + (
        ('اطلاعات تکمیلی', {
            'fields': (
                'phone',
                'avatar',
                'about_user',
                'address',
            )
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('اطلاعات تکمیلی', {
            'fields': (
                'phone',
                'avatar',
                'about_user',
                'address',
            )
        }),
    )