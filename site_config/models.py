from django.db import models
from django.db.models import CharField


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='نام سایت')
    site_url = models.URLField(verbose_name='آدرس سایت')
    country = models.CharField(max_length=300, verbose_name='شهر/کشور',default='ایران / تهران')
    address = models.CharField(max_length=300, verbose_name='آدرس')
    phone = models.CharField(max_length=200, blank=True, null=True, verbose_name='تلفن')
    fax = models.CharField(max_length=200, blank=True, null=True, verbose_name='فکس')
    email = models.EmailField(blank=True, null=True, verbose_name='ایمیل')
    email_text = models.CharField(blank=True, null=True, verbose_name='متن برای ایمیل')
    telegram_url = models.CharField( max_length=200,blank=True, null=True, verbose_name='لینک تلگرام')
    instagram_url = models.CharField( max_length=200,blank=True, null=True, verbose_name='لینک اینستاگرام')
    github_url = models.URLField(blank=True, null=True, verbose_name='لینک گیت هاب')
    linkedin_url = models.CharField( max_length=200,blank=True, null=True, verbose_name='لینک لینکدین')
    site_logo = models.ImageField(upload_to='images/site-setting/', verbose_name='لوگو سایت')
    favicon = models.ImageField(upload_to='images/site-setting/', blank=True, null=True, verbose_name='فاوآیکون سایت')
    copy_right = models.TextField(verbose_name='متن کپی رایت', blank=True, null=True)
    about_us_text = models.TextField(verbose_name='متن  درباره ما', blank=True, null=True)
    site_slogan = models.CharField(max_length=300, verbose_name='شعار سایت', blank=True, null=True)
    is_main_setting = models.BooleanField(default=False, verbose_name='تنظیمات اصلی',max_length=250)
    working_hours = models.CharField(max_length=300, verbose_name='ساعت کاری', blank=True, null=True)


    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات '





class  FooterKarmaGallery(models.Model):
    site = models.ForeignKey(SiteSetting, on_delete=models.CASCADE )
    title= models.CharField(max_length=300,blank=True,null=True,verbose_name='متن تیتر')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تصاویر گالری کارما فوتری'
        verbose_name_plural = 'گالری کارما '


class FooterKarmaGalleryList(models.Model):

    gallery = models.ForeignKey(
        FooterKarmaGallery,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='گالری تصاویر'

    )

    image = models.ImageField(
        upload_to='images/footer_karma_gallery/',verbose_name='تصویر'
    )

    def __str__(self):
        return 'گالری کارما'

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'گالری تصاویر'


class SiteBanner(models.Model):
    class SiteBannerPositions(models.TextChoices):
        PRODUCT_LIST = 'product_list', 'صفحه لیست محصولات'
        ARTICLE_LIST = 'article_list', 'لیست مقالات'
        ARTICLE_DETAIL = 'article_detail', 'صفحه جزئیات مقالات'

    title = models.CharField(max_length=200,verbose_name='عنوان بنر')
    url = models.CharField(max_length=400,null=True,blank=True,verbose_name='آدرس بنر')
    image = models.ImageField(upload_to='images/banners',verbose_name='تصویر بنر')
    is_active = models.BooleanField(default=True,verbose_name='فعال / غیرفعال')
    position = models.CharField(max_length=50,choices=SiteBannerPositions.choices,verbose_name='جایگاه نمایشی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بنر تبلیغاتی'
        verbose_name_plural = 'بنرهای تبلیغاتی'