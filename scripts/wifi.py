import network

ssid = input("SSID: ")
psk = input("PSK: ")

def main():
    lan = network.WLAN(network.STA_IF)
    lan.active(True)
    lan.connect(ssid, psk)
    lan.isconnected()

if __name__ == "__main__":
    main()

#################################

import network
essid = input("essid: ")
passwd = input("passwd: ")

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(essid, passwd)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

if __name__ == "__main__":
    do_connect()
