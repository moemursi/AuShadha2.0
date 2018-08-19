"""
Django settings for AuShadha project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

from __future__ import absolute_import
import sys
import os
import yaml

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR           = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_PATH          = os.path.dirname(__file__)
PARENT_ROOT        = os.path.abspath(os.path.join(ROOT_PATH, os.pardir))
APP_ROOT_URL       = u"/AuShadha/"
LOGIN_URL          = APP_ROOT_URL + u"authenticate/login/"
LOGIN_REDIRECT_URL = APP_ROOT_URL

SERIALIZATION_MODULES = {
    'yml': "django.core.serializers.pyyaml"
}

ADMINS = (
    ('Dr.Easwar T.R', 'dreaswar@gmail.com'),
)

MANAGERS = ADMINS

#AUTH_USER_MODEL = 'aushadha_users.AuShadhaUser'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i_x=+rho3+kn7imy8p7mykdx@7l^h10rs&ir^a^f4s*_wyphm@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []




# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'clinic.apps.ClinicConfig',
    'patient.apps.PatientConfig',
    'aushadha_base_models.apps.AushadhaBaseModelsConfig',
    'aushadha_users.apps.AushadhaUsersConfig',
    'aushadha_ui.apps.AushadhaUiConfig',
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

ROOT_URLCONF = 'AuShadha.urls'

SITE_ID = 1

TEMPLATES = [

    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'static'),
                 os.path.join(BASE_DIR, 'aushadha_ui/static'),
                 os.path.join(BASE_DIR, 'aushadha_users/static'),
                 ],
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

WSGI_APPLICATION = 'AuShadha.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'aushadha',
        'USER': 'aushadha',
        'PASSWORD': 'aushadha',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIR = [
    os.path.join(BASE_DIR, 'static'),
]
print(STATICFILES_DIR)
INSTALLED_APPS = (

# Core Django Apps used 
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

# Core AuShadha Apps, base_models, custom_users:
    'aushadha_ui',
    'aushadha_base_models',
    'aushadha_users',
    'clinic',
    'search',
    'patient'
)

try:
  ENABLED_APPS = yaml.load( open('AuShadha/configure.yaml').read() ) # This settings doesnt do anything now. 
except(IOError):
  ENABLED_APPS = list(INSTALLED_APPS)
  pass # Stupid hack just to let sphinx-apidoc pass this

UI_INITIALIZED = False
