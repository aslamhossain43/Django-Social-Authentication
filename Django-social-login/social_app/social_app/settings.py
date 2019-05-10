"""
Django settings for social_app project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(!xj_(r8t##)7s9@qnln+0wx&2@2#80t)c)!yxr@4u#%hmqb5#'

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
    'social_django', # add this
    'core' # add this
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


    #add this
AUTHENTICATION_BACKENDS = [

        'social_core.backends.facebook.FacebookOAuth2',# for facebook authentication
        'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
        'social_core.backends.google.GoogleOpenId',  # for Google authentication

        'social_core.backends.google.GoogleOAuth2',  # for Google authentication

        'django.contrib.auth.backends.ModelBackend',
    ]
  #add
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='159114385131-1tb6h15gkui8a8alrlf5saviutksklar.apps.googleusercontent.com'  #Paste CLient Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'asHPR2wCaaikSSGQVEF8xJe6' #Paste Secret Key
SOCIAL_AUTH_FACEBOOK_KEY = '413854835831673' # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '28833a3fa3f2cbc3a6b8655fedaa19fe'  # App Secret


ROOT_URLCONF = 'social_app.urls'

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
                'social_django.context_processors.backends', # add this
                'social_django.context_processors.login_redirect', # add this
            ],
        },
    },
]
 #for face book
SOCIAL_AUTH_FACEBOOK_KEY = '413854835831673'         # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '28833a3fa3f2cbc3a6b8655fedaa19fe'       # App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link'] # add this
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {       # add this
      'fields': 'id, name, email, picture.type(large), link'
    }
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [                 # add this
        ('name', 'name'),
        ('email', 'email'),
        ('picture', 'picture'),
        ('link', 'profile_url'),
    ]
# for google
SOCIAL_AUTH_FACEBOOK_KEY = '159114385131-1tb6h15gkui8a8alrlf5saviutksklar.apps.googleusercontent.com'
SOCIAL_AUTH_FACEBOOK_SECRET = 'asHPR2wCaaikSSGQVEF8xJe6'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'groups_access_member_info']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email',
    'edges': 'groups'
}
WSGI_APPLICATION = 'social_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
