import machine
import time

pin13 = machine.Pin(13, machine.Pin.IN)

while True:
    print(pin13.value())
    time.sleep_ms(1000)

#################################
# Movement Sensor

import machine
import time

pin13 = machine.Pin(13, machine.Pin.IN)

while True:
    if pin13.value() == 1:
        print('Movement Detected')
        time.sleep_ms(1000)
    else:
        print('All Clear')
        time.sleep_ms(1000)

#################################
# Sound Sensor

import machine
import time

pin13 = machine.Pin(13, machine.Pin.IN)

while True:
    if pin13.value() == 1:
        print('')
        time.sleep_ms(50)
    else:
        print('Sound Detected')
        time.sleep_ms(50)

#################################
