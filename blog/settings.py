from pathlib import Path
import os
import cloudinary
from cloudinary_storage.storage import MediaCloudinaryStorage

# -------------------------
# BASE DIRECTORY
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# SECRET & DEBUG
# -------------------------
SECRET_KEY = 'django-insecure-e=_1o1#$8cqq9knmw6h*v-_lo%7j287(muyyrt(ib@!+_)!t!5'
DEBUG = True

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = [
    "https://vue-blog-production.up.railway.app",
]

# -------------------------
# INSTALLED APPS
# -------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'articles',
    'users',
]



CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME', ''),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY', ''),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET', '')
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# # Add cloudinary apps only if environment variables exist
# if os.getenv('CLOUD_NAME') and os.getenv('CLOUD_API_KEY') and os.getenv('CLOUD_API_SECRET'):
#     INSTALLED_APPS += ['cloudinary', 'cloudinary_storage']
#     CLOUDINARY_STORAGE = {
#         'CLOUD_NAME': os.getenv('CLOUD_NAME'),
#         'API_KEY': os.getenv('CLOUD_API_KEY'),
#         'API_SECRET': os.getenv('CLOUD_API_SECRET'),
#     }
#     DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# else:
#     # Local dev fallback
#     DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# -------------------------
# MIDDLEWARE
# -------------------------
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------------
# CORS
# -------------------------
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "https://vue-blog-production.up.railway.app",
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = CORS_ALLOWED_ORIGINS

# -------------------------
# ROOT URLS & TEMPLATES
# -------------------------
ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'blog', 'templates'),
        ],
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

WSGI_APPLICATION = 'blog.wsgi.application'

# -------------------------
# DATABASE
# -------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------------
# AUTH PASSWORD VALIDATORS
# -------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# -------------------------
# INTERNATIONALIZATION
# -------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------------
# STATIC & MEDIA FILES
# -------------------------
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "blog" / "static"]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------------
# REST FRAMEWORK
# -------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication', 
    ]
}
