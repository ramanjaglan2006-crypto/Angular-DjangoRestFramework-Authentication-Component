from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# Use console backend for emails in development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
