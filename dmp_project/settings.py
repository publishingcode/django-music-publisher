"""
Django settings for dmp_project project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import csv
import os
import dj_database_url
from django.core.management.utils import get_random_secret_key
from decimal import Decimal
from music_publisher.validators import CWRFieldValidator

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', False)

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

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
    'whitenoise.middleware.WhiteNoiseMiddleware',
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

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3')))}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = os.getenv('STATIC_URL', '/static/')

STATIC_ROOT = os.getenv('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "dmp_project", "static"),
]

TIME_INPUT_FORMATS = [
    '%H:%M:%S',     # '14:30:59'
    '%M:%S',        # '14:30'
]

path = os.path.join(BASE_DIR, 'music_publisher', 'societies.csv')

with open(path, 'r') as f:
    reader = csv.reader(f)
    SOCIETIES = sorted(
        ((str(row[0]), '{} ({})'.format(row[1], row[2]))
         for row in reader),
        key=lambda row: row[1])

PUBLISHER_NAME = os.getenv('PUBLISHER', 'DJANGO-MUSIC-PUBLISHER')
PUBLISHER_CODE = os.getenv('PUBLISHER_CODE', '')

PUBLISHER_IPI_BASE = os.getenv('PUBLISHER_IPI_BASE', None)
PUBLISHER_IPI_NAME = os.getenv('PUBLISHER_IPI_NAME', '')

PUBLISHER_SOCIETY_MR = os.getenv('PUBLISHER_SOCIETY_MR', None)
PUBLISHER_SOCIETY_PR = os.getenv('PUBLISHER_SOCIETY_PR', None)
PUBLISHER_SOCIETY_SR = os.getenv('PUBLISHER_SOCIETY_SR', None)

REQUIRE_SAAN = os.getenv('REQUIRE_SAAN', False)
REQUIRE_PUBLISHER_FEE = os.getenv('REQUIRE_PUBLISHER_FEE', False)

PUBLISHING_AGREEMENT_PUBLISHER_PR = Decimal(
    os.getenv('PUBLISHER_AGREEMENT_PR', '0.5'))
PUBLISHING_AGREEMENT_PUBLISHER_MR = Decimal(
    os.getenv('PUBLISHER_AGREEMENT_PR', '1.0'))
PUBLISHING_AGREEMENT_PUBLISHER_SR = Decimal(
    os.getenv('PUBLISHER_AGREEMENT_PR', '1.0'))

SENTRY_DNS = os.getenv('SENTRY_DNS')

if SENTRY_DSN:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn="SENTRY_DSN",
        integrations=[DjangoIntegration()],
        send_default_pii=True
    )

    sentry_sdk.capture_message(f'Starting DMP for {PUBLISHER_NAME}')
