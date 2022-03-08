import os

from flask import Flask, url_for
from flask import request, after_this_request
from flask import make_response
from flask import render_template
from flask import abort, redirect

from markupsafe import escape
from werkzeug.utils import secure_filename

from src.database import init_db
from src.celery_utils import init_celery

from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.Config')

    init_db(app)

    return app

app = create_app()

# route setting
from src.routes import routes_setting
routes_setting(app)