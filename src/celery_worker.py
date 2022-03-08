from src import celery
from src.application import create_app
from src.celery_utils import init_celery

app = create_app()
init_celery(celery, app)