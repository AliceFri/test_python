from skill.rabbit_mq import connection

channel = connection.channel()


def callback(ch, method, properties, body):
    # print(ch, method, properties)
    # print(method.delivery_tag)
    print(f" [x] Received {body} {method.delivery_tag}")


if __name__ == '__main__':
    channel.queue_declare(queue='hello')
    # rabbitmqctl list_queues name messages_ready messages_unacknowledged

    tag = channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    # print(f"tag:{tag}")
    print(' [*] Waiting for messages. To exit press CTRL+C')

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
        connection.close()
        print(" [*] Exiting")
