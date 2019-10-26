import pika
import time

def on_message_callback(ch, method, properties, body):
    """

    Args:
        ch(:obj): pika.adapters.blocking_connection.BlockingChannel
        method(:obj:): pika.spec.Basic.Deliver
        properties(:obj:): 'pika.spec.BasicProperties'>
        body(bytes):

    Returns:

    """
    print(" [x] Received %r" % body)
    time.sleep(3)
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

rmq_host = '192.168.99.100'
rmq_port = '5672'

conn_params = pika.ConnectionParameters(rmq_host, rmq_port)
connection = pika.BlockingConnection(conn_params)

channel = connection.channel()
# Do not accept more than 1 message at a time
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='hello',
                      auto_ack=False,
                      on_message_callback=on_message_callback)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

