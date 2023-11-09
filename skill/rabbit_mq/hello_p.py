from skill.rabbit_mq import connection, channel

if __name__ == '__main__':
    # 创建一个（消息）队列
    channel.queue_declare(queue='hello')

    # In RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()
