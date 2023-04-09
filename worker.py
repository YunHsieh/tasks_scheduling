from celery import Celery
from celery.schedules import crontab
from datetime import timedelta
from environments import ADD_TASK_NAME, BROKER_URL, MULTIPLY_TASK_NAME, TOTAL_TASK_NAME

app = Celery('tasks')

default_config = 'celeryconfig'
app.config_from_object(default_config)

retry_kwargs = {
    "max_retries": 3,
    "retry_backoff": True,
}

app.conf.task_default_queue = 'default'
app.conf.task_default_exchange_type = 'direct'
app.conf.task_default_routing_key = 'default'

app.conf.beat_schedule = {
    'calculate_total_every_10_min': {
        'task': TOTAL_TASK_NAME,
        'schedule': crontab(minute='*/10'),
        'args': [1,2,3,4,5,6,7,8,9,10],
        'options': {'queue' : 'celery_periodic'},
    },
    'calculate_total_every_3_sec': {
        'task': TOTAL_TASK_NAME,
        'schedule': timedelta(seconds=3),
        'args': [1,2,3],
        'options': {'queue' : 'celery_periodic'},
    },
}

app.conf.timezone = 'UTC'
