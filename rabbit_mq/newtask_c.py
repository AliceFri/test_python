import time

import pika

credentials = pika.PlainCredentials('user', 'password')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost', port=5672, virtual_host='/', credentials=credentials
    )
)

channel = connection.channel()


def callback(ch, method, properties, body):
    print(f" [x] Received {body} {method.delivery_tag}")
    time.sleep(body.count(b'.'))
    print(f' [x] Done {method.delivery_tag}')
    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == '__main__':
    channel.queue_declare(queue='new_task')
    # rabbitmqctl list_queues name messages_ready messages_unacknowledged

    tag = channel.basic_consume(queue='new_task', on_message_callback=callback)
    # print(f"tag:{tag}")
    print(' [*] Waiting for messages. To exit press CTRL+C')

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
        connection.close()
        print(" [*] Exiting")
