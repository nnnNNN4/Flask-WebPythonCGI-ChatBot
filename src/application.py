import os

from flask import Flask, url_for
from flask_injector import FlaskInjector
from flask import request, after_this_request
from flask import make_response
from flask import render_template
from flask import abort, redirect

from markupsafe import escape
from werkzeug.utils import secure_filename

from src.database import init_db
from src.binds import configure
from src.celery_utils import init_celery

from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

PKG_NAME = os.path.dirname(os.path.realpath(__file__)).split('/')[-1]

def create_app(test_config=None, app_name=PKG_NAME, **kwargs):
    # create and configure the app
    app = Flask(
        app_name,
        instance_relative_config=True,
        instance_path='/Flask-Project-1/src/instance'
    )
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        config_object_string = 'src.config.DevelopmentConfig'
        if app.config['ENV'] == 'production':
            config_object_string = 'src.config.ProductionConfig'
        elif app.config['ENV'] == 'test':
            config_object_string = 'src.config.TestingConfig'

        app.config.from_object(config_object_string)
        # app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    init_db(app)
    if kwargs.get('celery'):
        init_celery(kwargs.get('celery'), app)

    # ensure the instance folder exists
    try:
        makedirs_not_exists(app.instance_path)
        makedirs_not_exists(app.config['FAQ_FILE_UPLOAD_DIR'])
        makedirs_not_exists(app.config['ML_VARS_DIR'])
    except OSError:
        pass

    # route setting
    from src.routes import routes_setting
    routes_setting(app)

    # DI
    FlaskInjector(app=app, modules=[configure])

    return app

def makedirs_not_exists(path: str):
    if os.path.exists(path):
        return

    os.makedirs(path)