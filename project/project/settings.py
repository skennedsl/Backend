"""
Django settings for project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&e6urx=f7b9qfc!c0usdaau#hvba5r6)uqb0r^mzt^h=0el!7f'

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get('DEBUG') == '1':
    DEBUG = True
else:
    DEBUG = False
# DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.64.2', '76.216.160.246']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'geoposition',
    'website',
    'api',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

try:
    DB_HOST = os.environ['PG_HOST']
except KeyError:
    DB_HOST = 'postgres'

try:
    DB_PORT = os.environ['PG_PORT']
except KeyError:
    DB_PORT = 5432

DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = os.environ.get('PG_PASS')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': DB_HOST,   # Or an IP Address that your DB is hosted on
        'PORT': DB_PORT,
    }
}

if os.environ.get('LOCAL') == '1':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#for geoposition
GEOPOSITION_MAP_OPTIONS = {
    'minZoom': 3,
    'center_on_current':True,
    'scrollwheel':True,
    'zoom':13,
    'center': {'lat': 38.5815719, 'lng': -121.49439960000001},
}

GEOPOSITION_MARKER_OPTIONS = {
    'cursor': 'move',
    'position_on_current':True,
    'position': {'lat': 38.5815719, 'lng': -121.49439960000001},
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = "/opt/Project/volatile/static/"
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

try:
    MEDIA_ROOT = os.environ['MEDIA_ROOT']
except:
    MEDIA_ROOT = '/opt/Project/persistent/media/'
    
MEDIA_URL = '/media/'
