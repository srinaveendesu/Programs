# Asynchronous Tasks with Flask and Celery, Redis, Rabbit MQ

Example of how to handle background processes with Flask, Celery,Redis, RabbitMQ and Docker.



Spin up the containers:

```sh
$ docker-compose up -d --build
```

Open your browser to [http://localhost:5004](http://localhost:5004) to view the app or to [http://localhost:5556](http://localhost:5556) to view the Flower dashboard.

Trigger a new task:

```sh
$ curl http://localhost:5004/tasks -H "Content-Type: application/json" --data '{"type": 0}'
```

Check the status:

```sh
$ curl http://localhost:5004/tasks/<TASK_ID>/
```
