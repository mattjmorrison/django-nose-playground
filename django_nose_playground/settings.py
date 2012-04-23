TEMPLATE_DEBUG = DEBUG = True
MANAGERS = ADMINS = ()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '.database',
    }
}

STATIC_ROOT = MEDIA_URL = MEDIA_ROOT = ''
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'w0@^s(5v=)+tar_3#+)twr%3=*r8j#jjt76mtpbu-q!9*vx4$+'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'django_nose_playground.urls'

WSGI_APPLICATION = 'django_nose_playground.wsgi.application'

PROJECT_APPS = (
    'sample',
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django_nose',
    'django_jenkins',
) + PROJECT_APPS

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
