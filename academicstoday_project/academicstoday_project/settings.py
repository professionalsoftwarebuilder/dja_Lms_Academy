"""
Django settings for academicstoday_project project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
from decouple import config, Csv

# Import variables for our application. Basically all imported variables
# have a SECRET_* prefix.
try:
    from academicstoday_project.secret_settings import *
except ImportError:
    pass

# Import all constants to use throughout our application
try:
    from academicstoday_project.constants import *
except ImportError:
    pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', cast=Csv())

# 'Sites Framework' requires this line.
SITE_ID = 1


# Application definition
#

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'account',
    'landpage',
    'registration',
    'login',
    'registrar',
    'student',
    'teacher',
    'ckeditor',
    'ckeditor_uploader',
    'publisher',
    'constance',
    'theBasis',
    'embed_video',
    'constance.backends.database',

)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'theBasis.middleware.AjaxMiddleware',
)

#    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',


ROOT_URLCONF = 'academicstoday_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'constance.context_processors.config',
            ],
        },
    },
]

WSGI_APPLICATION = 'academicstoday_project.wsgi.application'
#WSGI_APPLICATION = 'wsgi.application'



# Captcha App
#
# if 'test' in sys.argv:
#     CAPTCHA_TEST_MODE = True
# CAPTCHA_FONT_SIZE = 52



# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "academicstoday_db",
#         "USER": SECRET_DB_USER,
#         "PASSWORD": SECRET_DB_PASSWORD,
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Email
# http://stackoverflow.com/questions/19264907/python-django-gmail-smtp-setup

EMAIL_USE_TLS = True
EMAIL_HOST = SECRET_EMAIL_HOST
EMAIL_PORT = SECRET_EMAIL_PORT
EMAIL_HOST_USER = SECRET_EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = SECRET_EMAIL_HOST_PASSWORD
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
DEFAULT_TO_EMAIL = EMAIL_HOST_USER



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'nl-nl'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = False



# Static files (CSS, JavaScript, Images) & Upload Content
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_code"),
    os.path.join(BASE_DIR, "media_code"),
)

STATIC_ROOT = os.path.join(BASE_DIR, "static")

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CKEDITOR_UPLOAD_PATH = "ckeditor/"

CKEDITOR_CONFIGS = {
    'total': {
        'autoGrow_onStartup': True,
        'autoGrow_minHeight': 100,
        'autoGrow_maxHeight': 950,
        'extraPlugins': 'autogrow',
        'toolbar': 'full',
    },
    'default': {
            'toolbar': 'Custom',
            'toolbar_Custom': [
                ['Bold', 'Italic', 'Underline'],
                ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
                ['Link', 'Unlink'],
                ['RemoveFormat', 'Source']
            ]
        }
}

CKEDITOR_BROWSE_SHOW_DIRS = True

from .constance import *