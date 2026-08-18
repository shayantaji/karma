from django.db import models
from django.urls import reverse
from slugify import slugify

from account_module.models import User


class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    parent = models.ForeignKey("self",on_delete=models.CASCADE,blank=True,null=True,related_name="children")

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.title

    @property
    def has_children(self):
        return self.children.filter(is_active=True).exists()



class ProductBrand(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    image = models.ImageField(upload_to="brands/",blank=True,null=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "برند"
        verbose_name_plural = "برندها"

    def __str__(self):
        return self.title

class Product(models.Model):

    title = models.CharField(max_length=300)

    slug = models.SlugField(unique=True)

    category = models.ForeignKey(ProductCategory,on_delete=models.PROTECT,related_name="products")

    brand = models.ForeignKey(ProductBrand,on_delete=models.SET_NULL,null=True,blank=True,related_name="products")

    short_description = models.CharField(max_length=500)

    description = models.TextField()

    price = models.PositiveBigIntegerField()

    discount_percent = models.PositiveSmallIntegerField(default=0)

    inventory = models.PositiveIntegerField(default=0)

    weight = models.PositiveIntegerField(default=0,help_text="گرم")

    is_active = models.BooleanField(default=True)

    is_deleted = models.BooleanField(default=False)

    is_special = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]

        verbose_name = "محصول"

        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.title

    @property
    def final_price(self):
        if self.discount_percent == 0:
            return self.price

        return self.price - (
                self.price * self.discount_percent // 100
        )

    @property
    def is_in_stock(self):
        return self.inventory > 0

    @property
    def main_image(self):
        return self.images.filter(is_main=True).first()

    def get_absolute_url(self):
        return reverse('product_single', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)




class ProductImage(models.Model):

    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="images")

    image = models.ImageField(upload_to="products/")

    is_main = models.BooleanField(default=False)

    class Meta:
        verbose_name = "تصویر محصول"
        verbose_name_plural = "تصاویر محصولات"

    def __str__(self):
        return self.product.title

class ProductSpecification(models.Model):

    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="specifications")

    key = models.CharField(max_length=200)

    value = models.CharField(max_length=500)

    class Meta:
        verbose_name = "مشخصه"
        verbose_name_plural = "مشخصات"

    def __str__(self):
        return f"{self.product.title} - {self.key}"

class ProductComment(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments',verbose_name='محصول')

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='product_comments',verbose_name='کابر')

    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='replies',verbose_name='فرزند')

    text = models.TextField(verbose_name='متن پیام')

    is_approved = models.BooleanField(default=True,verbose_name='تایید/عدم تایید')

    created_date = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ نظر')

    class Meta:
        verbose_name = "نظرات محصول"
        verbose_name_plural = "نظرات محصولات"
        ordering = ['created_date']

