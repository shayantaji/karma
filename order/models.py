from django.db import models
from account_module.models import User
from product.models import Product


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name='نهایی شده/نشده', default=False)
    payment_date = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')
    first_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='نام')
    last_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='نام خانوادگی')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='شماره تلفن')
    email = models.EmailField(null=True, blank=True, verbose_name='ایمیل')
    address = models.TextField(null=True, blank=True, verbose_name='آدرس')
    postal_code = models.CharField(max_length=10, null=True, blank=True, verbose_name='کد پستی')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات سفارش')
    tracking_code = models.CharField(max_length=20, unique=True, null=True, blank=True, verbose_name='کد پیگیری')
    status = models.CharField(max_length=30, default='processing', verbose_name='وضعیت سفارش')

    def __str__(self):
        return str(self.user)

    def calculate_total_price(self):
        total_amount = 0

        if self.is_paid:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.final_price * order_detail.count
        else:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.product.final_price * order_detail.count

        return total_amount

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران'




class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    final_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی تکی محصول')
    count = models.IntegerField(verbose_name='تعداد')

    def get_total_price(self):
        return self.count * self.final_price

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural = 'لیست جزییات سبدهای خرید'
