import os

from celery import Celery


app = Celery("mbbloc_api")
app.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
app.conf.result_backend = os.environ.get(
    "CELERY_BACKEND_URL",
)

app.autodiscover_tasks()
