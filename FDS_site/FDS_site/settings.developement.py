try:
    from shared_settings import *
except ImportError:
    pass

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

ALLOWED_HOSTS = ['127.0.0.1']

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

TINYMCE_JS_URL = STATIC_URL + 'tinymce/tinymce.min.js'

TINYMCE_JS_ROOT = STATIC_ROOT + 'tinymce'