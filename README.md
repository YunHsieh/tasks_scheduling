# teaks_scheduling

```bash
docker-compose build
docker-compose up -d
```

tests work
```
docker-compose exec -it celery-worker  python comsumer/handler.py
```

if run up, try to connect the below monitoring.
```
(rabbitmq)[http://localhost:15672/#/connections]
(celery flower)[http://localhost:5555/flower/dashboard]
```
