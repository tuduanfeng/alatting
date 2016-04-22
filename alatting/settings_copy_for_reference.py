"""
Django settings for alatting project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!0wb8m-o^pew*o)hyho^zzy7f8m-94v%)4cxn4sa%e!gmp3+vw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

import alatting.pre_init

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.contrib.humanize',
    'rest_framework',
    'djcelery',
    'corsheaders',

    'alatting_website',
    'alatting_admin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

if DEBUG:
    MIDDLEWARE_CLASSES += ('utils.db.middleware.DatabaseMiddleware',)

ROOT_URLCONF = 'alatting.urls'

# Media files

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR + MEDIA_URL

# Templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [MEDIA_ROOT],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'alatting.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if DEBUG:
    DEFAULT_DB = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db1.sqlite3'),
    }
    DEFAULT_DB = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tianhu',
        'HOST':'alatting-mysql.cd5aq1se5ngs.us-west-2.rds.amazonaws.com',
        'PORT': '3306',
        'USER': 'alatting',
        'PASSWORD': 'Alatting_2015',
    }
else:
    DEFAULT_DB = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dev',
        'HOST':'alatting-mysql.cd5aq1se5ngs.us-west-2.rds.amazonaws.com',
        'PORT': '3306',
        'USER': 'alatting',
        'PASSWORD': 'Alatting_2015',
    }

DATABASES = {
    'default': DEFAULT_DB
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + STATIC_URL

# REST_FRAMEWORK
REST_FRAMEWORK = {

}

# login
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# CELERY
from celery.schedules import crontab
CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
CELERYBEAT_SCHEDULE = {
    'refresh-poster-everyday': {
        'task': 'alatting_website.tasks.poster',
        'schedule': crontab(hour=1, minute=58),
    },
}
# import djcelery
# djcelery.setup_loader()

from alatting import post_init