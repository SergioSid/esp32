import time
import network
import machine
from umqtt.simple import MQTTClient

ssid = input('ssid: ')
psk = input('psk: ')
pin13 = machine.Pin(13, machine.Pin.IN)

def connect():
    lan = network.WLAN(network.STA_IF)
    lan.active(True)
    if not lan.isconnected():
        print('connecting to network ...')
        lan.connect(ssid, psk)
        while not lan.isconnected():
            pass
    print('network config: ', lan.ifconfig())

def mosquitto(server = "192.168.1.115"):
    while True:
        mosq = MQTTClient("umqtt_client", server)
        mosq.connect()
        if pin13.value() == 1:
            mosq.publish(b"#", b"Movement Detected")
            time.sleep_ms(1000)
        else:
            mosq.disconnect()

if __name__ == "__main__":
    connect()
    mosquitto()

#################################

from umqtt.robust import MQTTClient

# Test reception e.g. with:
# mosquitto_sub -t foo_topic

def main(server="192.168.1.115"):
    c = MQTTClient("umqtt_client", server)
    c.connect()
    c.publish(b"test", b"hello")
    c.disconnect()

if __name__ == "__main__":
    main()
