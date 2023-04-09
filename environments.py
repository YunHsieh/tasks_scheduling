import os

BROKER_URL = os.getenv('BROKER_URL', 'amqp://guest:guest@rabbitmq:5672/')
BACKEND_URL = os.getenv('BACKEND_URL', 'rpc://')

ADD_TASK_NAME = 'comsumer.tasks.add'
MULTIPLY_TASK_NAME = 'comsumer.tasks.multiply'
TOTAL_TASK_NAME = 'comsumer.tasks.total'
