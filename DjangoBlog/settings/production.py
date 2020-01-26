from .common import *
import json

with open('/etc/django_blog_config.json') as config_file:
    config = json.load(config_file)

DEBUG = False

SECRET_KEY = config['DJANGO_BLOG_SECRET_KEY']

ALLOWED_HOSTS = ['localhost', '0.0.0.0']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

EMAIL_HOST_USER = config['EMAIL_USER']
EMAIL_HOST_PASSWORD = config['EMAIL_PASS']
