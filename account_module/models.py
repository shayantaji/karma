from django.db import models
from django.contrib.auth.models import AbstractUser




# Create your models here.


class User(AbstractUser):

    phone = models.CharField(max_length=11,unique=True,verbose_name="شماره موبایل")

    avatar = models.ImageField(upload_to='images/user_profile', verbose_name='تصویر آواتار', null=True, blank=True)

    about_user = models.TextField(null=True, blank=True, verbose_name='درباره شخص')

    address = models.TextField(null=True, blank=True, verbose_name='آدرس')

    USERNAME_FIELD = "phone"

    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()

        return self.username
