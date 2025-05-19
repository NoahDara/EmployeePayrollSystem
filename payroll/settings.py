from pathlib import Path
import os
import platform
import loguru

import environ
env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))  # Explicit path to .env

# environ.Env.read_env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'django.contrib.sites', 
    'allauth',
    'allauth.account',
    'allauth.socialaccount', 
    
    # local apps
    'accounts.apps.AccountsConfig',
    'audit.apps.AuditConfig',
    'bank.apps.BankConfig',
    'contracts.apps.ContractsConfig',
    'dashboard.apps.DashboardConfig',
    'demographics.apps.DemographicsConfig',
    'divisions.apps.DivisionsConfig',
    'employees.apps.EmployeesConfig',
    'employment.apps.EmploymentConfig',
    'organization.apps.OrganizationConfig',
    'positions.apps.PositionsConfig',
    'profiles.apps.ProfilesConfig',
    
    #3rd party apps
    "debug_toolbar",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'audit.middleware.NavigationTrackingMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'payroll.urls'
AUTH_USER_MODEL = 'accounts.CustomUser'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'payroll.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
MYSQL_DB_NAME = env("MYSQL_DB_NAME")
MYSQL_DB_USER = env("MYSQL_DB_USER")
MYSQL_DB_PASSWORD = env("MYSQL_DB_PASSWORD")
MYSQL_DB_HOST = env("MYSQL_DB_HOST")
MYSQL_DB_PORT = env("MYSQL_DB_PORT")
USE_MYSQL = env.bool("USE_MYSQL")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql" if USE_MYSQL else "django.db.backends.sqlite3",
        "NAME": MYSQL_DB_NAME if USE_MYSQL else BASE_DIR / "db.sqlite3",
        "USER": MYSQL_DB_USER if USE_MYSQL else None,
        "PASSWORD": MYSQL_DB_PASSWORD if USE_MYSQL else None,
        "HOST": MYSQL_DB_HOST if USE_MYSQL else None,
        "PORT": MYSQL_DB_PORT if USE_MYSQL else None,
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [BASE_DIR / "static"]

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.auth_backends.EmailOrUsernameModelBackend',
]

LOGIN_REDIRECT_URL = 'dashboard'
ACCOUNT_LOGOUT_REDIRECT = "login"

# Emails
EMAIL_BACKEND = env('EMAIL_BACKEND') 
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
EMAIL_USE_SSL= env('EMAIL_USE_TLS')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_SYSTEM_USER_EMAIL = env('DEFAULT_SYSTEM_USER_EMAIL')
DEFAULT_RECIPIENT = env('DEFAULT_RECIPIENT')

ADMINS = [
    ("noah", "noahdara2004@gmail.com"),]

path_separator = "\\" if platform.system() == "Windows" else "/"
ASN_FILE_DESTINATION = os.path.join(BASE_DIR, f"media{path_separator}asn{path_separator}")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
TEST_FILE_STORAGE = os.path.join(BASE_DIR, f"test-data{path_separator}results.xlsx")

STATUS_CHOICES = (('success', 'Success'), ('failed', 'Failed'),('pending', 'Pending'), ('rejected', 'Rejected'))

LOGGER = loguru.logger

DEBUG_TOOLBAR_ENABLED = env.bool("DEBUG_TOOLBAR_ENABLED", default=False)
if DEBUG_TOOLBAR_ENABLED:
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": lambda request: True  
    }
else:
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": lambda request: False  
    }
    
CSRF_TRUSTED_ORIGINS = [
    'https://*.ngrok-free.app'
]  
    
if not DEBUG:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "file": {
                "level": "ERROR",
                "class": "logging.FileHandler",
                "filename": os.path.join(BASE_DIR, "debug.log"),
            },
        },
        "loggers": {
            "django": {
                "handlers": ["file"],
                "level": "ERROR",
                "propagate": True,
            },
        },
    }
else:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": "{levelname} {name} {message}",
                "style": "{",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "simple",
            },
        },
        "loggers": {
            "": {  # root logger, catches all
                "handlers": ["console"],
                "level": "DEBUG",
            },
        },
    }
    
from helpers.task_manager import get_task_manager
TASK_MANAGER = get_task_manager()  

SITE_ID = 1