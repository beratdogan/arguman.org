"""
Django settings for arguman project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from datetime import timedelta

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qlp_henm3k-$7u@9b(@coqgpd1-2xmtox%a8_#*r9=0wh5d0oo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'social.apps.django_app.default',
    'django_gravatar',

    'profiles',
    'premises',
    'newsfeed',
    'blog',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'main.urls'

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'TR-tr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), "../static"),
)


TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "../templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

# Social Auth Settings
AUTHENTICATION_BACKENDS = (
    'social.backends.twitter.TwitterOAuth',
    'social.backends.github.GithubOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_USER_MODEL = 'profiles.Profile'
SOCIAL_AUTH_USER_MODEL = 'profiles.Profile'


CONTENT_DELETION = {
    'MAX_PREMISE_COUNT': 2,
    'HAS_EMPTY_CONTENT_DELETION': True,
    'LAST_DELETION_DATE': timedelta(hours=1)
}

SOCIAL_AUTH_TWITTER_KEY = None  # defined in settings_local.py
SOCIAL_AUTH_TWITTER_SECRET = None  # defined in settings_local.py

SOCIAL_AUTH_GITHUB_KEY = None  # defined in settings_local.py
SOCIAL_AUTH_GITHUB_SECRET = None  # defined in settings_local.py

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = None  # defined in settings_local.py
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = None  # defined in settings_local.py

SOCIAL_AUTH_FACEBOOK_KEY = None  # defined in settings_local.py
SOCIAL_AUTH_FACEBOOK_SECRET = None  # defined in settings_local.py

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'


SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.mail.mail_validation',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.debug.debug',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)


MONGODB_HOST = "localhost"
MONGODB_DATABASE = "arguman"

SITE_URL = "arguman.org"

# Markitup Settings
MARKITUP_SET = 'markitup/sets/markdown'
MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': False})

BLOG_FEED_TITLE = "Arguman.org Blog'u"
BLOG_FEED_DESCRIPTION = "Arguman analizi platformu"
BLOG_URL = "http://arguman.org/blog"

REPORT_DEACTIVATE_COUNT = 200

try:
    from settings_local import *
except ImportError:
    print "settings_local.py not found!"
