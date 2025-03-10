"""
Django settings for pm project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""


# Import dj-database-url at the beginning of the file.
#import dj_database_url

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#OLD SECRET_KEY = 'django-insecure-k%ts66p=#_lqw42d7&-jc^i%lreb7r0-9j#lc41t20+u9+y1mh'
SECRET_KEY = 'django-insecure-17zd-$!@sqo07p=xld)vtmd#!lnl5mwt*b=hk+ta-h^7*&myt8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'livereload',
    'django.contrib.staticfiles',
    'index.apps.IndexConfig',
    'django_summernote',
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
    # 'livereload.middleware.LiveReloadScript',
]

ROOT_URLCONF = 'pm.urls'
# ROOT_URLCONF = 'piecem.urls'

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
                'django.template.context_processors.media'
            ],
        },
    },
]

#Media files
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR, 'media/')

WSGI_APPLICATION = 'pm.wsgi.application'
# WSGI_APPLICATION = 'piecem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
#DATABASES = {
#   'default': dj_database_url.config(
#default= 'postgresql://pm:uFJ3V1aHzBcsujQG2b18Fe4kvtLFI353@dpg-cu2hlo1u0jms73d96ff0-a/pmdata_bxh8',
#conn_max_age= 600
#   )
#}



DATABASES = {
   'default': {
      'ENGINE': 'django.db.backends.sqlite3',
      'NAME': BASE_DIR / 'db.sqlite3',
   }
}

#DATABASES = {
#   'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
#}



# Replace the SQLite DATABASES configuration with PostgreSQL:
#DATABASES = {
 #   'default': dj_database_url.config(       
     # Replace this value with your local database's connection string.        
  #   default='postgresql://postgres:postgres@localhost:5432/mysite',        
   #  conn_max_age=600    )} 
   #'default': {
    #    'ENGINE': 'django.db.backends.postgresql',
     #   'NAME': 'datata',
      #  'USER': 'dev',
       # 'PASSWORD': '1234',
        #'HOST': 'localhost',
        #'PORT': '5432',
        #'client_encoding': 'UTF8'
    #}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


#STATIC_URL = '/static/'
# This production code might break development mode, so we check whether we're in DEBUG mode
#if not DEBUG:    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
#    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
#    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'







# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'index/static/index/'
STATIC_ROOT = os.path.join(BASE_DIR, 'index/static/index')


#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, 'index/static/index'),
#]
#if not DEBUG:    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
 #   STATIC_ROOT = os.path.join(BASE_DIR, 'index/static/index')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
  #  STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SUMMERNOTE editor configuration
#def summernote_custom_upload_to():
 #   return "inline/media/" + datetime.datetime.now().strftime("%Y/%m")

SUMMERNOTE_CONFIG = {

    'summernote': {
        # Toolbar customization
        # https://summernote.org/deep-dive/#custom-toolbar-popover
        #'attachment_upload_to': summernote_custom_upload_to(),
        'toolbar': [
            ['font', ['fontname','fontsize','bold','italic','forecolor','backcolor', 'clear']],
            ['height', ['height']],
            ['para', ['ul', 'ol', 'paragraph', 'style']],
            ['insert', ['link', 'picture']],
        ],
        'fontNames': ['NZ', 'Rubik'],
        'fontNamesIgnoreCheck': ['NZ', 'Rubik'],
        'colors' : [
            ['#f8ef88','#5cba9a','#f29799','#0d4048'], 
            ['white','black'] ,
        ],
        'fontSizes' : ['12','16','18','26','36','48','60'],
        'lineHeights' : ['0.7','1.2','2'],
       # 'style': ['Ombre Verte', 'Ombre jaune', 'Ombre rose', 'Ombre vert-canard'],
        'styleTags': [{ 'title': 'Ombre jaune','tag':'span', 'className': 'ombreJaune', 'value':'span'},
                { 'title': 'Ombre verte','tag':'span', 'className': 'ombreVerte', 'value':'span'},
                { 'title': 'Ombre rose','tag':'span', 'className': 'ombreRose', 'value':'span'},
                { 'title': 'Ombre vert-canard','tag':'span', 'className': 'ombreVertCanard', 'value':'span'}],
               },

}

