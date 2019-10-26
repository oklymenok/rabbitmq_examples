import pika

rmq_host = '192.168.99.100'
rmq_port = '5672'

conn_params = pika.ConnectionParameters(rmq_host, rmq_port)
connection = pika.BlockingConnection(conn_params)

channel = connection.channel()
# Durable queue allows messages to restart RabbitMQ server crash or restart
channel.queue_declare(queue='hello',durable=True)
# Also send messaget with persistent flag set
channel.basic_publish(exchange='',
                      routing_key='hello',
                      properties=pika.BasicProperties(
                          delivery_mode = 2, # make message persistent
                      ),
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()