class Config(object):
    TESTING = False

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
    SECRET_KEY = '...'

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SECRET_KEY = 'dev'

    # Somme
    HTTP_PLATFORM_PORT = 80

    # Mail config
    MAIL_SERVER = ''
    MAIL_PORT = ''
    MAIL_USE_TLS = ''
    MAIL_USE_SSL = ''
    MAIL_DEBUG = 1
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_DEFAULT_SENDER = ''
    MAIL_MAX_EMAILS = None
    MAIL_SUPPRESS_SEND = False
    MAIL_ASCII_ATTACHMENTS = False


class TestingConfig(Config):
    ENV = 'testing'
    DEBUG = True
    SECRET_KEY = 'test'
    TESTING = True