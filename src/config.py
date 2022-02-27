import os


class DevelopmentConfig:

    # Flask
    DEBUG = True

    # SQLAlchemy
    dbCOnfig = {
        'user': os.getenv('DB_USER', 'user'),
        'password': os.getenv('DB_PASSWORD', 'user'),
        'host': os.getenv('DB_HOST', 'mysql'),
        'database': os.getenv('DB_DATABASE', 'user'),
    }
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(
        **dbCOnfig)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

Config = DevelopmentConfig