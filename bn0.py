import time
import board
import busio
import adafruit_bno055
from bluetooth import *
import subprocess
import datetime
from time import gmtime, strftime
import os
import threading

class Bexample(threading.Thread):
    def __init__(self):
        super().__init__()
        self._kill = threading.Event()

    def run(self):

        i2c = busio.I2C(board.SCL, board.SDA)
        sensor = adafruit_bno055.BNO055(i2c)

        working_directory = os.getcwd()
        filepath = working_directory + '/sensordata.txt'
        
        print(filepath)
        print()
        f = open(filepath,'w+')

        while True:
            is_killed = self._kill.is_set()
            if is_killed:
                break;
   # print('Temperature: {} degrees C'.format(sensor.temperature))
   # print('Accelerometer (m/s^2): {}'.format(sensor.accelerometer))
   # print('Magnetometer (microteslas): {}'.format(sensor.magnetometer))
   # print('Gyroscope (deg/sec): {}'.format(sensor.gyroscope))
   # print('Euler angle: {}'.format(sensor.euler))
   # print('Quaternion: {}'.format(sensor.quaternion))
   # print('Linear acceleration (m/s^2): {}'.format(sensor.linear_acceleration))
   # print('Gravity (m/s^2): {}'.format(sensor.gravity))
   # print()
   
            time.sleep(1)
            print( strftime("%d %b %Y %H:%M:%S \n", gmtime()))
   
            f.write(strftime("%d %b %Y %H:%M:%S \n ", gmtime()))
        print("being Killed")

    def kill(self):
        self._kill.set()








