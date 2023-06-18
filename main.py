from common.utils import IncomingMessage, send_message_to_work_queue
from common.consumer import consume_queue
from src.cuarto_electrico import Electrical


def callback(channel, method, properties, body):
    contact_name, payload, number = IncomingMessage.get_info(body)
    command = payload.upper()

    if command == "/MEDIDORES":
        payload = Electrical.get_data()
        send_message_to_work_queue(contact_name, payload, number, channel, method, 'responses')
    else:
        payload = "Debe escribir: /MEDIDORES"
        send_message_to_work_queue(contact_name, payload, number, channel, method, 'responses')


if __name__ == '__main__':
    consume_queue(callback)


