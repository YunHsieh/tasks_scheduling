import os

BROKER_URL = os.getenv('BROKER_URL', 'amqp://guest:guest@localhost:5672/')
BACKEND_URL = os.getenv('BACKEND_URL', 'rpc://')
