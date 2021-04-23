
Setting up services

```docker-compose up```

This will bring up services worker, server and rabbit-mq.

The flask server is acting like a producer that will push a task to RabbitMQ server

Worker is responsible for receiving the messages. Any action based on msg would be writted here




Testing 


http://localhost:5000/create-job/<type ur message here>


when the above URL is hit we will be seeing messages in the console