# This is a (digitalio)-based library for the Classes, Objects, and Modules assignment.
# For the Classes, Objects, and Modules assignment, a main.py file was pre-made with the
# function of controlling a common anode RGB LED.
# The goal of the assignment was to create a functional library and class for the main.py code.

# This library is that class.

import digitalio
# This library is using (digialio), which works fine for making RGB colors go on or off, but not for
# modulating brightness.
import time


class RGB:

    def __init__(self, red_pin, green_pin, blue_pin):
        # The (__init__) code runs when an object/instance is created.
        # It provides arguments for the object to use.

        # The three arguments are the pins that will correspond to
        # the red, green, and blue RGB values.

        # The pins are part of a common anode RGB LED, in which a common power source (input)
        # is shared between the different pins (output).

        # It is important to note that an anode is a positively-charged electrode,
        # and a cathode is a negatively-charged electrode.

        # For these RGB pins, the anode is connected to +5v (input).
        # Because the RGB pins must be ground for the circuit to work (because current is created
        # by differences in voltage, the RGB pin values must be set to False or 0 to turn the RGB on.
        # If the RGB pins were set to True or 1, the current would not travel anywhere because
        # there would not be a significant difference in voltage.

        self.r = digitalio.DigitalInOut(red_pin)
        self.r.direction = digitalio.Direction.OUTPUT

        # The argument (r) must be (self.r) because there will be instances created from it, such as r1, r2, etc.
        # What the above code does is ensure that argument (r) will be a digital input-output pin and then

        # make it an output.

        self.g = digitalio.DigitalInOut(green_pin)
        self.g.direction = digitalio.Direction.OUTPUT

        self.b = digitalio.DigitalInOut(blue_pin)
        self.b.direction = digitalio.Direction.OUTPUT

    def red(self):
        # The common anode RGB LED will glow red - set red pin on and others off.
        self.r.value = False
        self.g.value = True
        self.b.value = True

    def magenta(self):
        # The common anode RGB LED will glow magenta  - set green pin off and others on.
        self.r.value = False
        self.g.value = True
        self.b.value = False

    def blue(self):
        # The common anode RGB LED will glow blue - set blue pin on and others off.
        self.r.value = True
        self.g.value = True
        self.b.value = False

    def cyan(self):
        # The common anode RGB LED will glow cyan - set red pin off and others on.
        self.r.value = True
        self.g.value = False
        self.b.value = False

    def green(self):
        # The common anode RGB LED will glow green - set green pin on and others off.
        self.r.value = True
        self.g.value = False
        self.b.value = True

    def yellow(self):
        # The common anode RGB LED will glow yellow - set blue pin off and others on.
        self.r.value = False
        self.g.value = False
        self.b.value = True

    def dark(self):
        # The common anode RGB LED will turn off
        self.r.value = True
        self.g.value = True
        self.b.value = True

    # Note - The method (rainbow) below in this code does not actually fade in and out of the rainbow
    # as the assignment asked for. The section below was optional, and while it would be nice to complete
    # it, the library (pulseio) is needed to so, which, as of now, has not been understood yet.

    # The method below makes the two common anode RGB LEDs cycle through a series of colors, one at a time, in
    # a loop; however, it does not cycle through the colors of the rainbow and does not fade.

    def rainbow(self, rate: float):
        # Here, variable to this method called rate is handed in, which is the reciprocal of the time
        # between colors. The colon after rate shows the data type that will be used.
        # In this case a float or floating point number (a number with a decimal point).

        # If the wrong data type was given, such as a string, Python would throw an error.
        # Even better, with PyCharm, the correct data type would be provided.

        self.yellow()
        # When using () after a method name, it calls that method from this method.
        time.sleep(1. / rate)
        self.green()
        time.sleep(1. / rate)
        self.blue()
        time.sleep(1. / rate)
        self.magenta()
        time.sleep(1. / rate)
        self.red()
        time.sleep(1. / rate)
