from celery import Celery
from environments import BROKER_URL

app = Celery('myapp')

default_config = 'celeryconfig'
app.config_from_object(default_config)

retry_kwargs = {
    "max_retries": 3,
    "retry_backoff": True,
}

app.conf.task_default_queue = 'default'
app.conf.task_default_exchange_type = 'direct'
app.conf.task_default_routing_key = 'default'
