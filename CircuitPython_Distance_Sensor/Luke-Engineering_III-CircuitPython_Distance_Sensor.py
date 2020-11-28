# This is my CircuitPython Distance Sensor code.

# Using digital io pins, so:

# import digitalio
# Why do I not need digitalio?
import time
import board
import adafruit_hcsr04
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

# The base ultrasonic distance sensor code was taken from;
# https://learn.adafruit.com/ultrasonic-sonar-distance-sensors/python-circuitpython

Sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

# Red_RGB_Value = str(int(float(Sonar.distance)
# Green_RGB_Value
# Blue_RGB_Value

while True:
    # Notes:
    # A (str) does not recognize numerical values, but rather reads...
    # ... them as a string of printable characters.
    # A (str) is required for printing something.
    # A floating point number can have a decimal, whereas an int...
    # ... will be a whole number.
    # The reason I needed to use (str) in the print function was...
    # ... because a print function does not read (int) or (float).
    try:
        print("Distance is " + str(int(float(Sonar.distance))))
        # Had to put a float before the int and then a str because...
        # the (Sonar.distance) was intended to be read as a string.
        # This code gives me a whole number string, which I...
        # ... can use now for RGB light function.

        # Helpful info on (if) statements from:
        # http://www.py4inf.com/html-008/cfbook004.html
        if int(float(Sonar.distance)) > 0 and int(float(Sonar.distance)) < 12:
            dot.fill((255, 0, 0))
            # When using an if or another similar key word such as...
            # ... (while True) the sentence must end with a colon (:).

        if int(float(Sonar.distance)) > 12 and int(float(Sonar.distance)) < 24:
            dot.fill((0, 0, 255))

        if int(float(Sonar.distance)) > 24 and int(float(Sonar.distance)) < 35:
            dot.fill((0, 255, 0))
            # For dot.fill, the intended order of color from 5 cm to...
            # ... 35 cm is red->pink->blue->light blue-> green.
            # Red is (255, 0, 0).
            # Pink is around ((255, 0, 255)).
            # Blue is around ((0, 0, 255)
            # Light blue is around ((0, 255, 255)).
            # Green is around ((0, 255, 0)).

    except RuntimeError:
        print("Retrying")
    time.sleep(2)