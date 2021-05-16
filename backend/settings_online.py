"""Django线上配置"""

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'HOST': '',
        'PORT': 3306,
        'USER': '',
        'PASSWORD': '',
    }
}

