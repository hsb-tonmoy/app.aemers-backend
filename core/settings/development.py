from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
import os

# --------------------------------------------------------------------------
# Loading .env file
# --------------------------------------------------------------------------

load_dotenv()

# --------------------------------------------------------------------------
# Build paths inside the project like this: BASE_DIR / 'subdir'.
# --------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------
# Loading the secret key
# --------------------------------------------------------------------------

SECRET_KEY = os.getenv('SECRET_KEY')

# --------------------------------------------------------------------------
# System-wide flags and configs
# --------------------------------------------------------------------------

DEBUG = True

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_TZ = True

USE_S3 = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --------------------------------------------------------------------------
# API Host Settings
# --------------------------------------------------------------------------

ALLOWED_HOSTS = []

# --------------------------------------------------------------------------
# User Model
# --------------------------------------------------------------------------

AUTH_USER_MODEL = 'accounts.Accounts'

# --------------------------------------------------------------------------
# SITE ID
# --------------------------------------------------------------------------

SITE_ID = 1

# --------------------------------------------------------------------------
# CORS Settings
# --------------------------------------------------------------------------

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CSRF_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True


# --------------------------------------------------------------------------
# Django Apps
# --------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
]

THIRD_PARTY_APPS = [
    'import_export',
    'rest_framework',
    'drf_spectacular',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'django_filters',
    'corsheaders',
    'storages',
    'post_office',
    'simple_history',
    'notifications',
    'imagekit',
    'django_messages_drf',
    'django_q'
]

LOCAL_APPS = [
    'apps.accounts',
    'apps.notes',
    'apps.file_opening',
    'apps.document_submission',
    'apps.pre_application_form',
    'apps.i_20_upload',
    'apps.ds_160',
    'apps.sevis_payment',
    'apps.visa_fee_payment',
    'apps.visa_interview',
    'apps.pre_departure_session',
    'apps.mock_visa_interview',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# --------------------------------------------------------------------------
# Django Middleware
# --------------------------------------------------------------------------


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

# --------------------------------------------------------------------------
# URLCONF
# --------------------------------------------------------------------------

ROOT_URLCONF = 'core.urls'

# --------------------------------------------------------------------------
# TEMPLATES
# --------------------------------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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
    {
        'BACKEND': 'post_office.template.backends.post_office.PostOfficeTemplates',
        'APP_DIRS': True,
        'DIRS': [],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
            ]
        }
    }
]

# --------------------------------------------------------------------------
# Email Backend
# --------------------------------------------------------------------------

POST_OFFICE = {
    'TEMPLATE_ENGINE': 'post_office',
    'MESSAGE_ID_ENABLED': True,
    'MAX_RETRIES': 4,
    'RETRY_INTERVAL': timedelta(minutes=5),
    'DEFAULT_PRIORITY': 'now',
}


EMAIL_BACKEND = 'post_office.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_USE_TLS = True
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

# --------------------------------------------------------------------------
# WSGI
# --------------------------------------------------------------------------

WSGI_APPLICATION = 'core.wsgi.application'


# --------------------------------------------------------------------------
# Database Config
# --------------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': os.getenv('ENGINE'),
        'NAME': os.getenv('NAME'),
        'USER': os.getenv('USER'),
        'PASSWORD': os.getenv('PASSWORD'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT'),
    }
}

# --------------------------------------------------------------------------
# Password Validators
# --------------------------------------------------------------------------

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

# --------------------------------------------------------------------------
# REST Framework
# --------------------------------------------------------------------------

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (

        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

}

# --------------------------------------------------------------------------
# DRF Documentation
# --------------------------------------------------------------------------

SPECTACULAR_SETTINGS = {
    'TITLE': 'app-aemers-api',
    'DESCRIPTION': 'REST API for app.aemers.com',
    'VERSION': '1.0.0',
}

# --------------------------------------------------------------------------
# DRF Authentication
# --------------------------------------------------------------------------

ACCOUNT_ADAPTER = 'apps.accounts.adapter.CustomAccountAdapter'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
OLD_PASSWORD_FIELD_ENABLED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_SUBJECT_PREFIX = "app.aemers.com - "

ACCOUNT_EMAIL_CONFIRMATION_URL = os.getenv('ACCOUNT_EMAIL_CONFIRMATION_URL')

REST_USE_JWT = True
JWT_AUTH_COOKIE = 'access'
JWT_AUTH_REFRESH_COOKIE = 'refresh'

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'apps.accounts.serializers.CustomUserDetailsSerializer',
    'PASSWORD_RESET_SERIALIZER': 'apps.accounts.serializers.CustomPasswordResetSerializer',
}

# REST_AUTH_REGISTER_SERIALIZERS = {
#     'REGISTER_SERIALIZER': 'apps.accounts.serializers.RegistrationSerializer',
# }

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),

    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'AUTH_HEADER_TYPES': ('JWT',),
}

# --------------------------------------------------------------------------
# Social Authentication
# --------------------------------------------------------------------------


GOOGLE_OAUTH_CALLBACK_URL = os.getenv('GOOGLE_OAUTH_CALLBACK_URL')


# --------------------------------------------------------------------------
# AWS Storage Backend
# --------------------------------------------------------------------------

if USE_S3:
    # aws settings
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_SIGNATURE_VERSION = 's3v4'
    AWS_S3_REGION_NAME = 'us-east-1'
    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_S3_FILE_OVERWRITE = False
    # s3 static settings
    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'core.storage_backends.StaticStorage'
    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'core.storage_backends.PublicMediaStorage'
else:
    STATIC_URL = '/staticfiles/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_URL = '/mediafiles/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)


# --------------------------------------------------------------------------
# Django Notifications
# --------------------------------------------------------------------------

DJANGO_NOTIFICATIONS_CONFIG = {'SOFT_DELETE': True}

# --------------------------------------------------------------------------
# Django-Q
# --------------------------------------------------------------------------

Q_CLUSTER = {
    'name': 'app.aemers',
    'recycle': 500,
    'timeout': 120,
    'retry': 240,
    'compress': True,
    'save_limit': 1000,
    'label': 'Django Q',
    'orm': 'default',

}
