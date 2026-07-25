
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('contact-us/', include('contact.urls')),
    path('articles/', include('article.urls')),
    path('products/', include('product.urls')),
    path('user/',include('account_module.urls')),


]


urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)