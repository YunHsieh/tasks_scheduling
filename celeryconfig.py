from kombu import Queue, Exchange
from environments import ADD_TASK_NAME, BROKER_URL, MULTIPLY_TASK_NAME

CELERY_RESULT_BACKEND = 'rpc://'
BROKER_URL = BROKER_URL
CELERY_IMPORTS = ['comsumer.tasks']

BROKER_CONNECTION_MAX_RETRIES = 3

CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('addition', Exchange('addition'), routing_key='addition'),
    Queue('multiplication', Exchange('multiplication'), routing_key='multiplication'),
)

# define a queue
CELERY_ROUTES = {
    ADD_TASK_NAME: {'queue': 'addition', 'routing_key': 'addition'},
    MULTIPLY_TASK_NAME: {'queue': 'multiplication', 'routing_key': 'multiplication'},
}

CELERY_ANNOTATIONS = {
    ADD_TASK_NAME: {'rate_limit': '10/s'}
}

BROKER_CONNECTION_MAX_RETRIES = 3
