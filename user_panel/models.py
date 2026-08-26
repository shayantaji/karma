from django.db import models

from account_module.models import User
from product.models import Product


# Create your models here.


class UserFavorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='کاربر'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='محصول'
    )

    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاریخ افزودن'
    )

    class Meta:
        verbose_name = 'علاقه مندی'
        verbose_name_plural = 'علاقه مندی ها'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'product'],
                name='unique_favorite'
            )
        ]

    def __str__(self):
        return f'{self.user} - {self.product}'