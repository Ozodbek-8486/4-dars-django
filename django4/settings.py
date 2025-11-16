from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-ew3$3%89ey#z8^po4mzu$$6jqs8+ka@p=dk6wb80xh@v!pw2_@'

DEBUG = True

APPEND_SLASH = True



AUTH_USER_MODEL = "users.CustomUser"





ALLOWED_HOSTS = ["*"]  

INSTALLED_APPS = [

    "jazzmin",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'users',
    'book',
    "django.contrib.staticfiles",
    
    

 
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

ROOT_URLCONF = 'django4.urls'





TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates",
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

WSGI_APPLICATION = 'django4.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


LANGUAGE_CODE = 'uz'
TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



LOGOUT_REDIRECT_URL = '/'   


LOGIN_URL = "users:login"

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"] 
STATIC_ROOT = BASE_DIR / "staticfiles"   

MEDIA_URL = '/media/'
MEDIA_ROOT =  "media-fayllar"  
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/users/login/'


JAZZMIN_SETTINGS = {
    "site_title": "Books market admin page",
    "site_header": "Admin saxifasi",
    "site_brand": "Book app",
    "welcome_sign": "Assalom alekum, admin...",
    "show_sidebar": True,
    "navigation_expanded": True,
    "custom_css": "admin/css/hacer.css",
    "custom_js": "admin/js/main.js",
    "icons": {
        "book.Book": "fas fa-book",
    },
}

JAZZMIN_UI_TWEAKS = {
    "theme": "cyborg",         
    "dark_mode_theme": "cyborg",
    "navbar": "navbar-dark",
    "sidebar": "sidebar-dark-primary",
    "brand_colour": "navbar-dark",
}