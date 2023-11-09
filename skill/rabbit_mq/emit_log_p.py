import sys

import pika

credentials = pika.PlainCredentials('user', 'password')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost', port=5672, virtual_host='/', credentials=credentials
    )
)
channel = connection.channel()


if __name__ == '__main__':
    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    message = ' '.join(sys.argv[1:]) or "Hello World!"
    channel.basic_publish(exchange='logs', routing_key='', body=message)
    print(" [x] Sent %r" % message)
    connection.close()
