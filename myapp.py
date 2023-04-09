'''
Mock outside to call the celery task.
'''
from celery import Celery
from environments import ADD_TASK_NAME, BACKEND_URL, BROKER_URL

app = Celery('myapp')
app.conf.broker_url = BROKER_URL
app.conf.result_backend = BACKEND_URL

# the queue is needed that will tell the worker to run.
result = app.send_task(ADD_TASK_NAME, args=[1, 2], queue='addition')
print(result.get())
