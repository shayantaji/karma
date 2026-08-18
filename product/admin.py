from django.contrib import admin
from product.models import *


class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ['user','product']
    list_editable = ['product']

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification
    extra = 1



class ProductAdmin(admin.ModelAdmin):

    list_display = ['title', 'category', 'brand', 'price', 'inventory', 'is_active']

    list_filter = ['category', 'brand', 'is_active', 'is_special']

    search_fields = ['title', 'brand__title']

    list_editable = ['price', 'inventory', 'is_active']

    inlines = [ProductImageInline, ProductSpecificationInline]



class ProductCategoryAdmin(admin.ModelAdmin):

    list_display = ['title', 'is_active']

    list_filter = ['is_active']

    search_fields = ['title']

    list_editable = ['is_active']



class ProductBrandAdmin(admin.ModelAdmin):

    list_display = ['title', 'is_active']

    list_filter = ['is_active']

    search_fields = ['title']

    list_editable = ['is_active']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductBrand, ProductBrandAdmin)
admin.site.register(ProductComment,ProductCommentAdmin)
