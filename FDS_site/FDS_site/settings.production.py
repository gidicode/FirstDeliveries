try:
    from shared_settings import *
except ImportError:
    pass

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fllsdnqe_FIRST_LOGISTICS',
        'USER': env('PRODUCTION_USER'),
        'PASSWORD': env('PRODUCTION_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

ALLOWED_HOSTS = ['flls.ng', 'www.flls.ng']

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/fllsdnqe/public_html/media/'

TINYMCE_JS_URL = STATIC_URL + 'tinymce/tinymce.min.js'

TINYMCE_JS_ROOT = STATIC_ROOT + 'tinymce'