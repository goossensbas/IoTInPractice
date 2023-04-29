import network
import machine
from machine import I2C
import bme280

iot_ssid = 'bvnetwerk'
iot_passwd = 'xLbCMeZtac'

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
print( "NIC status: ", sta_if.active())

if not sta_if.isconnected():
    sta_if.connect('bvnetwerk', 'xLbCMeZtac')
    while not sta_if.isconnected():
        pass
print(sta_if.isconnected())
print(sta_if.ifconfig())

bus = I2C(1, scl = machine.Pin(22), sda = machine.Pin(21))

bme = bme280.BME280(i2c = bus)
print(bme.temperature)

