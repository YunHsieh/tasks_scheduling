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
    # time.sleep(5)
    self.update_state(state=states.PENDING)
    time.sleep(10)
    return x * y
