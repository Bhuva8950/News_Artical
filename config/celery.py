from celery import Celery

app = Celery(
    "artical",
    broker="memory://",
    backend="cache+memory://",
)