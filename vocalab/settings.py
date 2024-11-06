import os
from pathlib import Path
from dotenv import load_dotenv

# vocalab/settings.py

TIME_ZONE = 'Europe/Paris'  
USE_TZ = True 


# Load environment variables from .env file
load_dotenv()

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key configuration
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'votre_clé_secrète_par_défaut')

# Debug setting
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'  # Mettre False en production

# Allowed hosts
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',') if not DEBUG else []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Pour django-allauth
    'accounts',
    'quiz',
    'dashboard',
    'django_extensions',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.microsoft',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Middleware d'authentification par Django
    'allauth.account.middleware.AccountMiddleware',  # Middleware de django-allauth
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'vocalab.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'vocalab' / 'templates',  # Assurez-vous que ce chemin correspond à la structure du projet
            BASE_DIR / 'accounts' / 'templates',  # Ajout du chemin vers les templates de l'application accounts
        ],
        'APP_DIRS': True,  # Assurez-vous que ce paramètre est à True
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

WSGI_APPLICATION = 'vocalab.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'nl'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    str(BASE_DIR / "static"),
]

# formulaire pour signin
ACCOUNT_FORMS = {
    'signup': 'accounts.forms.CustomSignupForm',
}

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = str(BASE_DIR / 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # Backend par défaut de Django
    'allauth.account.auth_backends.AuthenticationBackend',  # Backend Allauth
)

SITE_ID = 1

# URL de redirection après connexion/déconnexion
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Configuration des comptes utilisateurs

ACCOUNT_USERNAME_REQUIRED = True  # Active le champ username
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # Utilise l'email pour l'authentification
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"  # Vous pouvez ajuster selon vos besoins


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
