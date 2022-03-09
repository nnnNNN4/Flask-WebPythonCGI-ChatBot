import os

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    FAQ_FILE_UPLOAD_DIR = '/Flask-Project-1/src/upload'

    CELERY = {
        'broker': 'redis://redis:6379',
        'backend': 'redis://redis:6379',
        'imports': ['src.admin.domain.tasks'],
    }

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):

    # Flask
    DEBUG = True

    # SQLAlchemy
    dbCOnfig = {
        'user': os.getenv('DB_USER', 'user'),
        'password': os.getenv('DB_PASSWORD', 'user'),
        'host': os.getenv('DB_HOST', 'mysql'),
        'database': os.getenv('DB_DATABASE', 'user'),
    }
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/mydb?charset=utf8'.format(
        **dbCOnfig)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

class TestingConfig(Config):
    TESTING = True


def get_config(env='development'):
    if env == 'production':
        return ProductionConfig()
    elif env == 'test':
        return TestingConfig()
    else:
        return DevelopmentConfig()