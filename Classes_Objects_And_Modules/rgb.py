# This is my library for the Classes, Objects, and Modules assignment.
# The goal is to create the class /RGB/ and define it.

import digitalio
import time


class RGB:

    def __init__(self, red_pin, green_pin, blue_pin):
        # The three arguments are the different values,
        # which are red, green, and blue,
        # That will make the common anode RGB change color.
        # An anode is a positively charged electrode.
        # For these LEDs, the anode is connected to +5v.
        # So to make current flow, we need the appropriate
        # color pin to be connected to 0v (ground) - which is
        # will happen if we set that output's value to False, not True.

        self.r = digitalio.DigitalInOut(red_pin)
        self.r.direction = digitalio.Direction.OUTPUT

        self.g = digitalio.DigitalInOut(green_pin)
        self.g.direction = digitalio.Direction.OUTPUT

        self.b = digitalio.DigitalInOut(blue_pin)
        self.b.direction = digitalio.Direction.OUTPUT

    def red(self):
        # glow red
        self.r.value = False
        self.g.value = True
        self.b.value = True

    def magenta(self):
        # glow magenta - set green pin off and others on
        self.r.value = False
        self.g.value = True
        self.b.value = False

    def blue(self):
        # glow blue - set blue pin on and others off
        self.r.value = True
        self.g.value = True
        self.b.value = False

    def cyan(self):
        # glow cyan - set red pin off and others on
        self.r.value = True
        self.g.value = False
        self.b.value = False

    def green(self):
        # glow green - set green pin on and others off
        self.r.value = True
        self.g.value = False
        self.b.value = True

    def yellow(self):
        # glow yellow - set blue pin off and others on
        self.r.value = False
        self.g.value = False
        self.b.value = True

    def dark(self):
        # Turn LED off
        self.r.value = True
        self.g.value = True
        self.b.value = True

    def rainbow(self, rate: float):
        # Here I hand in a variable to this method called rate, which is the reciprocal of the time
        # between colors. The colon after rate shows the data type I want to use, in this case a float.
        # If we were to hand in a variable of incorrect type, for example a string, Python would throw an error
        # (or in my case, PyCharm would warn me of an error)

        self.yellow()
        # when using () after a method name, it calls
        # that method from this method.
        time.sleep(1. / rate)
        self.green()
        time.sleep(1. / rate)
        self.blue()
        time.sleep(1. / rate)
        self.magenta()
        time.sleep(1. / rate)
        self.red()
        time.sleep(1. / rate)
