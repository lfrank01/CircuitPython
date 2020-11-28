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

# The trigger and echo pin measure ultrasonic distance:
# The trigger pin creates an ultranonic pulse.
# The echo pin recieves the ultrasonic pulse when it is reflected...
# ... and creates a pulse read by the HC-SR04 that is proportional...
# ... to the time it took for the ultrasonic pulse to bounce back.
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

    # I found in the (adafruit_hcsr04) file that the (.distance)...
    # ... function is by default a (float) data type. I converted...
    # ... it to an (str) for the (print) function.

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
        # Red (255, 0, 0) -> Pink (255, 0, 255) -> Blue (0, 0, 255)...
        # ... -> Light Blue (0, 255, 255) -> Greeb (0, 255, 0).

        # It is also important to note that there are four color...
        # ... changes since there are four arrows. This means...
        # ... that each color change will be in a (35) - (5)...
        # ... interval divided by four, so each change is over (7.5 cm).

        # ----------------------------------------------------------

        if Distance < 12.5:

            # Note that after (if) statement, there must be a colon.
            # This section is for red to pink.

            red = 255
            green = 0
            blue = max(0,int(((Distance - 5) / Step_size) * 255))

            # I make the (distance) back to an (int)..
            # ... for the RGB function.

            # Using the (max) function allows the light to read...
            # ... distances below (5) cm without the RGB value...
            # ... becoming negative.

        if Distance > 12.5 and Distance < 20:
            # This section is for pink to blue.

            red = 255 - int(((Distance - 12.5) / Step_size) * 255)
            green = 0
            blue = 255

            # Note that the (Distance) must be subtratced by...
            # the highest data point of the last piece of code...
            # so that the data range will always be in between...
            # ... (0) and (255).

        if Distance > 20 and Distance < 27.5:
            # This section is for blue to light blue.

            red = 0
            green = int(((Distance - 20) / Step_size) * 255)
            blue = 255

        if Distance > 27.5:
            # This section is for light blue to green.

            red = 0
            green = 255
            blue = max(0,255 - int(((Distance - 27.5) / Step_size) * 255))

            # The max function makes it so the RGB value will not go...
            # ... above (255).

        dot.fill((red, green, blue))

        # Only one (dot.fill((red, green, blue))) is needed because...
        # ... the if statement will only apply new conditions...
        # to the code, not create a loop.

    except RuntimeError:
        print("Retrying")

    time.sleep(0.2)
