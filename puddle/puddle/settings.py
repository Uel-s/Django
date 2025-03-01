import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# Security configurations for web service in render.
DEBUG = os.environ.get("DEBUG", "False").lower()=="true"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split()

SECRET_KEY = os.environ.get("SECRET_KEY", "AS7h0sWqmXE2LnNaNx7VrHO6w9myhAve@dpg")
database_url = os.environ.get("DATABASE_URL")

LOGIN_URL = "/login/" # unauthorized persons redirect to login.
LOGIN_REDIRECT_URL = "/" # redirect to front page when logged in.
LOGOUT_REDIRECT_URL = "/" # redirect to front page when logged in.


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'conversation',
    'core',
    'dashboard',
    "item", 
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

ROOT_URLCONF = 'puddle.urls'

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

WSGI_APPLICATION = 'puddle.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# SQLite db

# overriding SQLite with PostgreSQL db

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "puddle_vic6",
       "HOST":"dpg-cuvb2ii3esus73bnme70-a.frankfurt-postgres.render.com",
       "USER":"puddle_vic6_user",
       "PASSWORD":"AS7h0sWqmXE2LnNaNx7VrHO6w9myhAve",
       "PORT":"5432"
    }
}





# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# Configurations for adding image
MEDIA_URL = 'media/'
MEDIA_ROOT= BASE_DIR / 'media'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
