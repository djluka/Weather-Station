import pigpio
from lib import DHT22
from time import sleep
from bmp280 import BMP280
from db import mysql_conn, create_table, insert_data 

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

pi = pigpio.pi()

dht22 = DHT22.sensor(pi, 4)
dht22.trigger()

def readDHT22():
    dht22.trigger()
    DHT22humidity = '%2.f' % (dht22.humidity())
    #DHT22temp = '%2.f' % (dht22.temperature())
    #return(DHT22humidity, DHT22temp)
    return DHT22humidity

bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

conn = mysql_conn()
create_table(conn)

while True:
    sleep(1)
    ##DHT22humidity, DHT22temperature = readDHT22()
    humidity = readDHT22()
    temperature = bmp280.get_temperature()
    pressure = bmp280.get_pressure()

    insert_data(conn, temperature, humidity, pressure)

    print("Himidity is :" , humidity + "%")
    print('Temperature is :{:0.0f} C '.format(temperature))
    print('Pressure is : {:0.0f}hPa'.format(pressure))
    print("-"*50)
