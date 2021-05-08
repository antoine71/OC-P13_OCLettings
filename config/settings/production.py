import os

from .base import *  # noqa


# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
DEBUG = False
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['oc-lettings-2.herokuapp.com']

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
# SECURE_SSL_REDIRECT = True
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True
