from kombu import Queue, Exchange
from environments import BROKER_URL

CELERY_RESULT_BACKEND = 'rpc://'
BROKER_URL = BROKER_URL
CELERY_IMPORTS = ['comsumer.tasks']

BROKER_CONNECTION_MAX_RETRIES = 3

CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('addition', Exchange('addition'), routing_key='addition'),
    Queue('multiplication', Exchange('multiplication'), routing_key='multiplication'),
)

CELERY_ROUTES = {
    'comsumer.tasks.add': {'queue': 'addition', 'routing_key': 'addition'},
    'comsumer.tasks.multiply': {'queue': 'multiplication', 'routing_key': 'multiplication'},
}

CELERY_ANNOTATIONS = {
    'comsumer.tasks.add': {'rate_limit': '10/s'}
}

BROKER_CONNECTION_MAX_RETRIES = 3
