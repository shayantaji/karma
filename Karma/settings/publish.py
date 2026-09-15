from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    'kkarma.ir',
    'www.kkarma.ir',
]

CSRF_TRUSTED_ORIGINS = [
    'https://kkarma.ir',
    'https://www.kkarma.ir',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'uboytlgw_karma_project_db',
        'USER': 'uboytlgw_shayan11exe',
        'PASSWORD': 'Def11esteghlal',
        'OPTIONS': {
            'autocommit': True,
        }
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = '/home/uboytlgw/public_html/static'

MEDIA_URL = '/uploads/'
MEDIA_ROOT = '/home/uboytlgw/public_html/uploads'