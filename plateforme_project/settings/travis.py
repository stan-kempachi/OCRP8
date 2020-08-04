from . import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
     },
} 


SELENIUM_WEBDRIVERS = {
'default': {
'callable': chrome.Chrome,
'args': (),
'kwargs': {},
},
}