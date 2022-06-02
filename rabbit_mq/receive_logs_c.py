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

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='logs', queue=queue_name)

    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body} {method.delivery_tag}")

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()
