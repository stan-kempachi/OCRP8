import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'plateforme_project.settings'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "k=*?viYl)?\x0czx'r)inQhsSpo>x6xQ'H[V\x0cTvZqz_d!>:b2Qv"

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

INSTALLED_APPS = [
    'pbeurre',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'debug_toolbar',
    'widget_tweaks',
    'django_crontab',
    'anymail',
]

ROOT_URLCONF = 'plateforme_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'pbeurre/templates')],
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

TEMPLATE_DIRS = (
    'plateforme_project/pbeurre/templates',
)

WSGI_APPLICATION = 'plateforme_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pbeurre',
        'USER': 'Stan',
        'PASSWORD': 'Kempachi94',
        'HOST': 'localhost',
        'PORT': '5432',
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

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

INTERNAL_IPS = []

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

LOGIN_URL = 'pbeurre:login'

CRONJOBS = [
    ('59 23 */7 * *', 'django.core.management.call_command', ['cm_db']),
]

# Anymail
SITE_ID = 1

ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "MAILJET_API_KEY": 'ffa15c5d3160d95a43b357f18192a8ea',
    "MAILJET_SECRET_KEY": 'd6a222a6040d613fb9d38858501de385',

}

EMAIL_BACKEND = "anymail.backends.mailjet.EmailBackend"  # or sendgrid.EmailBackend, or...
DEFAULT_FROM_EMAIL = "stan.ali@hotmail.fr"  # if you don't already have this in settings
SERVER_EMAIL = "stan.ali@hotmail.fr"  # ditto (default from-email for Django errors)
MAILJET_API_URL = "https://api.mailjet.com/v3"
