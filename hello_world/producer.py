import pika

rmq_host = '192.168.99.100'
rmq_port = '5672'

conn_params = pika.ConnectionParameters(rmq_host, rmq_port)
connection = pika.BlockingConnection(conn_params)

channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()