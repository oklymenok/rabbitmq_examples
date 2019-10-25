import pika

def on_message_callback(ch, method, properties, body):
    """

    Args:
        ch(:obj): pika.adapters.blocking_connection.BlockingChannel
        method(:obj:): pika.spec.Basic.Deliver
        properties(:obj:): 'pika.spec.BasicProperties'>
        body(bytes):

    Returns:

    """
    print(type(ch))
    print(type(method))
    print(type(properties))
    print(type(body))
    print(body)

rmq_host = '192.168.99.100'
rmq_port = '5672'

conn_params = pika.ConnectionParameters(rmq_host, rmq_port)
connection = pika.BlockingConnection(conn_params)

channel = connection.channel()
channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=on_message_callback)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

