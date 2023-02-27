"""
Django settings for cantera project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

from .local_settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '68e(dg592gr+(@b&t07qzcf9k__c*+%+^_qcyc(*0t&h$x=ob2'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.twitter',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
    
    'actualidad',
    'evento',
    'publicaciones',
    'organizaciones',
    'foro',
    'galerias',
    'puntosvista',
    'users.apps.UsersConfig',
    'configuracion',
    'solicitudes',
    'compromisos',

    #aplicaciones de terceros
    'sorl.thumbnail',
    'taggit',
    'taggit_autosuggest',
    'ckeditor',
    'ckeditor_uploader',
    'location_field.apps.DefaultConfig',
    'embed_video',
    'solo',
    'el_pagination',
    'crispy_forms',
    'disqus',
    'compressor',
    'nested_admin',
    'colorfield',
    'haystack', 
    'django_crontab',
]

AUTH_USER_MODEL = 'users.User'

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'cantera.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cantera.context.imagenes',
            ],
        },
    },
]

WSGI_APPLICATION = 'cantera.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'es-ni'

TIME_ZONE = 'America/Managua'

USE_I18N = True

USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

MEDIA_ROOT = os.environ.get('MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))
MEDIA_URL = '/media/'
STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))
STATIC_URL = '/static/'

STATICFILES_DIRS = (
   os.path.join(BASE_DIR, "static_media"),
)

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', ],#'user_friends'
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        # 'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.12',
    },
     'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'extraPlugins': ','.join([
            # 'image2',
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'embed',
            'autoembed',
            
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
        'toolbar': [
            { 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ], 'items': [ 'Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates' ] },
            { 'name': 'clipboard', 'groups': [ 'clipboard', 'undo' ], 'items': [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ] },
            { 'name': 'editing', 'groups': [ 'find', 'selection', 'spellchecker' ], 'items': [ 'Find', 'Replace', '-', 'SelectAll', '-', 'Scayt' ] },
            #{ 'name': 'forms', 'items': [ 'Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField' ] },
            '/',
            { 'name': 'basicstyles', 'groups': [ 'basicstyles', 'cleanup' ], 'items': [ 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat' ] },
            { 'name': 'paragraph', 'groups': [ 'list', 'indent', 'blocks', 'align', 'bidi' ], 'items': [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language' ] },
            { 'name': 'links', 'items': [ 'Link', 'Unlink', 'Anchor' ] },
            { 'name': 'insert', 'items': [ 'Image', 'Youtube', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe' ] },
            '/',
            { 'name': 'styles', 'items': [ 'Styles', 'Format', 'Font', 'FontSize' ] },
            { 'name': 'colors', 'items': [ 'TextColor', 'BGColor' ] },
            { 'name': 'tools', 'items': [ 'Maximize', 'ShowBlocks', ] },
             {
    }

        ],
        'height': '300px',
        'width': 'auto',
    },

}

LOCATION_FIELD_PATH = STATIC_URL + 'location_field'

LOCATION_FIELD = {
    'map.provider': 'openstreetmap',
    'map.zoom': 15,

    'search.provider': 'nominatim',
    'search.suffix': '',

    # OpenStreetMap
    'provider.openstreetmap.max_zoom': 18,

    # misc
    'resources.root_path': LOCATION_FIELD_PATH,
    'resources.media': {
        'js': [
            LOCATION_FIELD_PATH + '/js/jquery.livequery.js',
            LOCATION_FIELD_PATH + '/js/form.js',
        ],
    },
}

ACCOUNT_FORMS = {
    'signup': 'users.forms.CustomUserCreationForm',
}


AUTH_USER_MODEL = 'users.User'
# SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'

DISQUS_API_KEY = '2dwFxEqkNjZtNAxRr9Sa4jfknLONQrwXL5zl5fleL0od7Vhdyl2WRo9rZsbhDMwE'
DISQUS_WEBSITE_SHORTNAME = 'https-generoymetodologias-org'

COMPRESS_ENABLED = False
COMPRESS_ROOT = STATIC_ROOT
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

FILE_UPLOAD_PERMISSIONS = 0o644

TAGGIT_CASE_INSENSITIVE = True

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 12

# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.BaseSignalProcessor'

WHOOSH_INDEX = os.path.join(BASE_DIR, 'whoosh/')

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': WHOOSH_INDEX,
    },
}

THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.wand_engine.Engine'
THUMBNAIL_PRESERVE_FORMAT = True

CRONJOBS = [
    ('0 1 * * *', 'django.core.management.call_command', ['rebuild_index']),
]