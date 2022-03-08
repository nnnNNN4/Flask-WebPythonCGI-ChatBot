## SQLAlchemy起動チェック
from src import application
import src

app = application.create_app(celery=src.celery)
app.run()