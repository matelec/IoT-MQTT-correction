from umqtt_simple import MQTTClient
import time

class MqttConnection:
    def __init__(self, broker, identite, port, topic, user, password):
        self.broker= broker
        self.identite= identite
        self.port= port
        self.topic= topic
        self.user= user
        self.password= password

    def startMQTT(self,message):
        client = MQTTClient(
            self.identite,
            self.broker,
            self.port,
            self.user,
            self.password
        )

        # publication sur le topic
        try:
            client.connect()
            print("Connected au broker MQTT avec succes!")
            client.publish(self.topic, message)
            time.sleep(1)
            client.disconnect()
        except Exception as e:
            print("Erreur lors de la connexion au broker MQTT :", e)