import os
from os.path import join
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import cloudinary
import cloudinary.uploader
import cloudinary.api

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c-hlw)&shxag_6i*i1xtbrtqe9f5zfexs2k0ji1(hcp%x^64eg'
# SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = bool(os.environ.get('DEBUG'))

# ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(' ')
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

# for heroku add: 'erp-demo.herokuapp.com', # erp-demo is the name of the app


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'zorov_hub.main_app',
    'cloudinary',
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
# for heroku add on top     'whitenoise.middleware.WhiteNoiseMiddleware',


ROOT_URLCONF = 'zorov_hub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'zorov_hub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# same name as the DB created!
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'zorov_hub_db',         # same name as the DB created
        'USER': 'postgres-user',
        'PASSWORD': 'password',
        'HOST': 'localhost',    # Not host.docker.internal - only for pgadmin
        'PORT': '5432',
    }
}

# # heroku gives custom info for the db
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'd7pque6llenjil',
#         'USER': 'gfglkealwnywlh',
#         'PASSWORD': '61f32a79a35f8925e65e11fd6433249f668b21062ae2640c59a3f7c3dc2aafaa',
#         'HOST': 'ec2-54-77-40-202.eu-west-1.compute.amazonaws.com',
#         'PORT': '5432',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': os.environ.get('DB_ENGINE'),
#         'NAME': os.environ.get('DB_NAME'),
#         'USER': os.environ.get('DB_USER'),
#         'PASSWORD': os.environ.get('DB_PASSWORD'),
#         'HOST': os.environ.get('DB_HOST'),
#         'PORT': os.environ.get('DB_PORT'),
#     }
# }

CACHES = {
    'default': {
        'BACKEND':
            'django.core.cache.backends.redis.RedisCache',
        'LOCATION':
            'redis://127.0.0.1:6379',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    join(BASE_DIR, 'staticfiles'),
)

# for heroku use this (the folder must be static, not staticfiles)
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#
# STATIC_URL = '/static/'
# STATICFILES_DIRS = (
#     join(BASE_DIR, 'static'),
# )

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media_files'

# heroku
cloudinary.config(
    cloud_name="hpnglbxlz",
    api_key="713429118316855",
    api_secret="veB_dwVAE954b9yeyx3rCUNnV2o",
    secure=True,
)
# syshto corrention in models and the links for the file in templates


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'add profile'

LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'
