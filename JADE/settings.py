import os
from pathlib import Path

# Directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-key'

DEBUG = True

ALLOWED_HOSTS = []


# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Tu aplicación local para JADE & GOWK
    'tienda',
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

ROOT_URLCONF = 'JADE.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Si decides centralizar templates fuera de la app, puedes usar BASE_DIR / 'templates'
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'JADE.wsgi.application'


# Base de datos (SQLite3 por defecto)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = []


# Configuración de idioma y hora (Español de México)
LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_TZ = True


# ==========================================
# CONFIGURACIÓN DE ARCHIVOS ESTÁTICOS (CSS, JS)
# ==========================================
STATIC_URL = 'static/'

# Directorio donde Django buscará archivos estáticos adicionales globales
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


# ==========================================
# CONFIGURACIÓN DE MULTIMEDIA (FOTOS DE ROPA Y PERFILES)
# ==========================================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ==========================================
# CONTROL DE FLUJO DE USUARIOS (NUEVO)
# ==========================================
# A dónde redirige Django automáticamente cuando usas @login_required
LOGIN_URL = 'login'

# A dónde manda al usuario después de poner su contraseña correctamente
LOGIN_REDIRECT_URL = 'inicio'

# A dónde lo manda al cerrar sesión
LOGOUT_REDIRECT_URL = 'inicio'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'