from dataclasses import dataclass
from dataclass_wizard import JSONWizard
from from_dict import from_dict
import json


@dataclass
class IncomingMessage:
    sender: str
    payload: str
    number: str

    @staticmethod
    def get_info(body: bytes):
        my_dict = json.loads(body.decode())
        result: IncomingMessage = from_dict(IncomingMessage, my_dict)
        contact_name = result.sender
        payload = result.payload
        number = result.number
        return contact_name, payload, number


@dataclass
class OutgoingMessage(JSONWizard):
    sender: str
    payload: str
    number: str

    @staticmethod
    def set_info(contact_name, response_message, number):
        message = OutgoingMessage(contact_name, response_message, number).to_json()
        return message


@dataclass
class User:
    contacts: dict


def send_message_to_work_queue(contact_name: str, response_message: str, number: str, channel, method, queue: str):
    data = OutgoingMessage.set_info(contact_name, response_message, number)
    channel.basic_publish(exchange='', routing_key=queue, body=data)
    if method is not None:
        channel.basic_ack(delivery_tag=method.delivery_tag)

    print(f" [x] Sent\n quee--> {queue}\n' {data}'")
