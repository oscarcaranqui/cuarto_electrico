import paho.mqtt.subscribe as subscribe
from v1.layout import DOCUMENT

class Electrical:

    @staticmethod
    def get_data():
        try:
            ce_taura_3_energy_meter = "taura_3/1/ultima_muestra"
            ce_taura2_energy_meter = "taura_2/1/ultima_muestra"
            ce_california_energy_meter = "california/1/ultima_muestra"
            ce_churute_energy_meter = "churute/1/ultima_muestra"

            topic = [ce_california_energy_meter, ce_churute_energy_meter, ce_taura_3_energy_meter,
                     ce_taura2_energy_meter]
            message_received = subscribe.simple(topics=topic,
                                                hostname="192.168.1.40",
                                                port=1886,
                                                client_id="client_siemav",
                                                keepalive=180,
                                                msg_count=4)

            result = DOCUMENT.write_pdf(message_received)

        except Exception as e:
            result = "Personal se encuentra manipulando la data, inténtelo de nuevo porfavor"
            print(e)

        return result








