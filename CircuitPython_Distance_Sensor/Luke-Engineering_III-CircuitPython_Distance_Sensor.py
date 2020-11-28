# This is my CircuitPython HC-SRO4 Ultrasonic Distance Sensor code.

import board
import adafruit_hcsr04
# The link to adafruit_hcsr04:
# https://github.com/adafruit/Adafruit_CircuitPython_HCSR04/blob/master/adafruit_hcsr04.py
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

# The link to the websitw with the base...
# ... ultrasonic distance sensor code is listed below:

# https://learn.adafruit.com/ultrasonic-sonar-distance-sensors/python-circuitpython

Sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
# Created an object for measuring the function of (.distance).

while True:

    # Notes on the different data types that were used, which were...
    # ... (str), (float), and (int):

    # The (str) stands for (string). It does not read numerical values...
    # ... but rather converts all of its data into a printable format.
    # The (str) data type is required for (print) functions.

    # The (float) stands for (floating point). It includes a demcial and...
    # ... any value, such as (8.) that includes a decimal will be...
    # considered a floating point number unless told otherwise.

    # The (int) stands for (integer). It is a whole number and it is...
    # ... important to note that it will always convert a decimal value,...
    # ... whether it be greater than or less than (.5), to the first...
    # ... lowest integer. For example, (8.9) would become (8).

    Distance = Sonar.distance

    # I found in the (adafruit_hcsr04) file that the (.distance) function...
    # ... is by default a (float) data type. I converted it to an (str) for...
    # the (print) function.

    try:
        print("Distance is " + str(round(Distance)))

        # The (round) function rounds a decimal up to the nearest integer...
        # if it greater than or equal to (0.5). It was used for to...
        # achieve better distance reading accuracy.

        # RGB values (from 0 to 255) are integers, so what the above...
        # ... code does is round the (float) decimal and then print...
        # ... that number as an (str) data type.

        Step_size = 7.5
        # By adding a decimal after the (7), the value is...
        # ... set as a (float) data point.

        # ----------------------------------------------------------

        # The upcoming code is creating a neopixel RGB color based...
        # ... on the (distance) reading from (5) to (35).

        # NeoPixel was mentioned earlier as (board.NEOPIXEL, 1).

        # The (distance) reading is starting at (5 cm) because...
        # the HC-SR04 has trouble reading (distance) when it...
        # ... is any closer.

        # Between (5 cm) and (35 cm), the neopixel will do this:
        # Red (255, 0, 0) -> Pink (255, 0, 255) -> Blue (

        if Distance < 12.5:
            # This section changes red to pink.
            red = 255
            green = 0
            blue = max(0,
                       int(((Distance - 5) / Step_size) * 255)
                       )  # if 5cm then blue is 0 but must not go below 0
            # When using an if or another similar key word such as...
            # ... (while True) the sentence must end with a colon (:).

        if Distance > 12.5 and Distance < 20:
            # go from pink to blue
            red = 255 - int(((Distance - 12.5) / Step_size) * 255)
            # varies red from 255 to 0 in this range
            green = 0
            blue = 255

        if Distance > 20 and Distance < 27.5:
            # from blue to light blue
            red = 0  # varies btw 0 and 255
            green = int(((Distance - 20) / Step_size) * 255)
            blue = 255

        if Distance > 27.5:
            # from light blue to green
            red = 0  # varies btw 0 and 255
            green = 255
            blue = max(0,
                       255 - int(((Distance - 27.5) / Step_size) * 255)
                       )  # blue mustnt go below 0 even if distance is large

        dot.fill((red, green, blue))

    except RuntimeError:
        print("Retrying")

    time.sleep(0.2)