# teaks_scheduling

## Celery + RabbitMQ + Celery Flower

## Goals
1. Build docker for control worker
2. Implement queue get task
3. Mock outside project request a task
4. Use crontab to call the task

```bash
docker-compose build
docker-compose up -d
```

#### tests
```bash
# try the task
docker-compose exec -it celery-base  python comsumer/handler.py
# try the outside project send the task
docker-compose exec -it celery-base  python myapp.py
```

### if run up, try to connect the below monitoring locally.
[rabbitmq](http://localhost:15672/#/connections) 
[celery flower](http://localhost:5555/flower/dashboard)


## Refer
[Celery git](https://github.com/celery/celery) 
[Celery configuration parameters](https://docs.celeryq.dev/en/stable/userguide/configuration.html#std-setting-beat_schedule) 

## Diagram
