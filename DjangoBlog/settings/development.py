from .common import *

DEBUG = True

SECRET_KEY = os.environ.get('DJANGO_BLOG_SECRET_KEY')

ALLOWED_HOSTS = ['localhost', '0.0.0.0']

EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
