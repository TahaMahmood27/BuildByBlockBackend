import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

ALLOWED_HOSTS = ['*']
DEBUG = True

STATIC_URL = "/static/"
STATIC_ROOT = '/home/ubuntu/static'
STATICFILES_DIRS = ['/home/ubuntu/fyp_backend/static', ]

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/ubuntu/media'