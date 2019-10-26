# Requirements

* Python 3

# Set up lab environment

* Start docker machine
 docker-machine start

* Start RabbitMQ server in Docker
 docker run -d --name rabbitmq-server -p 5672:5672 rabbitmq

# Run the code

* Create virtualenv
  make venv

# Run RabbitMQ commands

* Check queues
  docker exec -ti rabbitmq-server rabbitmqctl list_queues

* Print messages_unacknowledged
  docker exec -ti rabbitmq-server rabbitmqctl list_queues name messages_ready messages_unacknowledged
