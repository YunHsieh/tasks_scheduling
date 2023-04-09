import sys
sys.path.append(".")
from worker import app, retry_kwargs
from celery import states
import time


@app.task(bind=True, autoretry_for=(Exception,), retry_kwargs=retry_kwargs)
def add(self, x, y):
    self.update_state(state=states.PENDING)
    return x + y


@app.task(bind=True, autoretry_for=(Exception,), retry_kwargs=retry_kwargs)
def multiply(self, x, y):
    self.update_state(state='PROGRESS', meta={'progress': 50})
    time.sleep(10)
    return x * y


@app.task(bind=True, autoretry_for=(Exception,), retry_kwargs=retry_kwargs)
def total(self, *args):
    print('the schedule is working')
    return sum(args)
