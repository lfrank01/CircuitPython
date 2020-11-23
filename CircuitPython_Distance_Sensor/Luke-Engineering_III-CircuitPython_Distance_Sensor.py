# This is my CircuitPython Distance Sensor code.

# Using digital io pins, so:

import digitalio
import time
import board
import adafruit_hcsr04

# This code was taken from;
# https://learn.adafruit.com/ultrasonic-sonar-distance-sensors/python-circuitpython
Sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    time.sleep(2)