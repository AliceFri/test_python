import pika

credentials = pika.PlainCredentials('user', 'password')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost', port=5672, virtual_host='/', credentials=credentials
    )
)
channel = connection.channel()

# rabbitmqctl list_exchanges
# rabbitmqctl list_queues name messages_ready messages_unacknowledged
# rabbitmqctl list_bindings

if __name__ == '__main__':
    print(connection)
    print(channel)
