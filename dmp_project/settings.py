"""
Django settings for dmp_project project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'nosjouthfjhrwfureiwzzw452uih52k4j')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'music_publisher.apps.MusicPublisherConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dmp_project.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'dmp_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES['default'] = dj_database_url.config(default='sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3')))


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.getenv('STATIC_ROOT', os.path.join(BASE_DIR, "static"))

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "dmp_project", "static"),
]

MUSIC_PUBLISHER_SETTINGS = {
    'admin_show_publisher': True,
    'admin_show_saan': True,

    'enforce_saan': True,
    'enforce_publisher_fee': True,
    'enforce_pr_society': True,
    'enforce_ipi_name': True,

    'token': os.getenv('TOKEN', None),
    'validator_url': os.getenv('VALIDATOR_URL', None),
    'generator_url': os.getenv('GENERATOR_URL', None),
    'highlighter_url': os.getenv('HIGHLIGHTER_URL', None),

    'work_id_prefix': '',

    'publisher_id': 'FOO',
    'publisher_name': 'FOO S MUSIC PUBLISHING',
    'publisher_ipi_name': '00000000199',
    'publisher_pr_society': '071',
    'publisher_mr_society': '034',
    'publisher_sr_society': None,

    'us_publisher_override': {
        'ASCAP': {
            'publisher_id': 'FOOA',
            'publisher_name': 'FOO A MUSIC PUBLISHING',
            'publisher_ipi_name': '00000000493',
            'publisher_pr_society': '010',
            'publisher_mr_society': '034',
            'publisher_sr_society': None,
        },
        'BMI': {
            'publisher_id': 'FOOB',
            'publisher_name': 'FOO B MUSIC PUBLISHING',
            'publisher_ipi_name': '00000000395',
            'publisher_pr_society': '021',
            'publisher_mr_society': '044',
            'publisher_sr_society': None,
        },
        'SESAC': None,
    },

    'library': 'FOO BAR MUSIC LIBRARY',
    'label': 'FOO BAR MUSIC',
}

TIME_INPUT_FORMATS = [
    '%H:%M:%S',     # '14:30:59'
    '%M:%S',        # '14:30'
]

try:
    from .local_settings import *
except ImportError:
    pass
