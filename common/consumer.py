from common.settings import SETTINGS
import pika

USERNAME = SETTINGS.rabbitmq_user
PASSWORD = SETTINGS.rabbitmq_pass
HOST = SETTINGS.rabbitmq_host
PORT = SETTINGS.rabbitmq_port
QUEUE = SETTINGS.my_queue


def connect():
    credentials = pika.PlainCredentials(USERNAME, PASSWORD)
    parameters = pika.ConnectionParameters(host=HOST, port=PORT, credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    return connection, channel


def close_channel(channel):
    print('Closing the channel')
    channel.close()


def close_connection(connection):
    print('Closing connection')
    connection.close()


def consume_queue(callback):
    connection, channel = connect()
    channel.basic_consume(queue=QUEUE, on_message_callback=callback)

    try:
        print("Waiting messages.....")
        channel.start_consuming()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
    finally:
        if channel.is_open:
            print('channel closed')
            close_channel(channel)
        if connection.is_open:
            print('connection closed')
            close_connection(connection)






