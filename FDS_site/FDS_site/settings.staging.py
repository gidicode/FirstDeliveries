try:
    from shared_settings import *
except ImportError:
    pass

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fllsdnqe_test',
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASS'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

ALLOWED_HOSTS = ['runtest.flls.ng', 'www.runtest.flls.ng']

STATIC_URL = '/static/'
STATIC_ROOT = '/home/fllsdnqe/runtest.flls.ng/static/FDS_app'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TINYMCE_JS_URL = STATIC_URL + 'tinymce/tinymce.min.js'

TINYMCE_JS_ROOT = STATIC_ROOT + 'tinymce'