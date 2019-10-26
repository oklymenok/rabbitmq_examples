import pika

rmq_host = '192.168.99.100'
rmq_port = '5672'

conn_params = pika.ConnectionParameters(rmq_host, rmq_port)
connection = pika.BlockingConnection(conn_params)

channel = connection.channel()
# Declare fanout exchange
channel.exchange_declare(exchange='hello', exchange_type='fanout')
# Declare queues
channel.queue_declare(queue='test_1', durable=True)
channel.queue_declare(queue='test_2', durable=True)
# Declare binding
channel.queue_bind(exchange='hello', queue='test_1')
channel.queue_bind(exchange='hello', queue='test_2')
# Publish to exchange
channel.basic_publish(exchange='hello',
                      routing_key='',        # Routing key is ignored when fanout exchange is used
                      properties=pika.BasicProperties(
                          delivery_mode = 2, # make message persistent
                      ),
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()