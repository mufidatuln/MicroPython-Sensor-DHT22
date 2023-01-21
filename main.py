from machine import Pin
from time import sleep
import dht 

sensor = dht.DHT22(Pin(14))
pin_led = Pin(13, mode=Pin.OUT)

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    print('Temperature: %3.1f C' %temp)
    print('Humidity: %3.1f %%' %hum)
    print(' ')
    if temp < 38:
        pin_led.off()
        print("Lampu Menyala")
    else:
        pin_led.on()
