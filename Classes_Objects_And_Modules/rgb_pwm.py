# This is a (pulseio)-based library for the Classes, Objects, and Modules assignment.

# For the Classes, Objects, and Modules assignment, a main.py file was pre-made with the
# function of controlling a common anode RGB LED.
# The goal of the assignment was to create a functional library and class for the main.py code.

# This library is that class.

# Note - The library does NOT work, currently.

import pulseio
# This library is using (pulseio), which works fine for making RGB colors go on or off, but not for
# modulating brightness.
import time



class RGB_PWM:

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

        self.r = pulseio.PWMOut(red_pin, frequency=500)

        # The argument (r) must be (self.r) because there will be instances created from it, such as r1, r2, etc.
        # What the above code does is ensure that argument (r) will be a digital input-output pin and then

        # make it an output.

        self.g = pulseio.PWMOut(green_pin, frequency=500)

        self.b = pulseio.PWMOut(blue_pin, frequency=500)

    def red(self):
        # The common anode RGB LED will glow red - set red pin on and others off.
        self.r.duty_cycle = 0
        self.g.duty_cycle = 65535
        self.b.duty_cycle = 65535

    def magenta(self):
        # The common anode RGB LED will glow magenta  - set green pin off and others on.
        self.r.duty_cycle = 0
        self.g.duty_cycle = 65535
        self.b.duty_cycle = 0

    def blue(self):
        # The common anode RGB LED will glow blue - set blue pin on and others off.
        self.r.duty_cycle = 65535
        self.g.duty_cycle = 65535
        self.b.duty_cycle = 0

    def cyan(self):
        # The common anode RGB LED will glow cyan - set red pin off and others on.
        self.r.duty_cycle = 65535
        self.g.duty_cycle = 0
        self.b.duty_cycle = 0

    def green(self):
        # The common anode RGB LED will glow green - set green pin on and others off.
        self.r.duty_cycle = 65535
        self.g.duty_cycle = 0
        self.b.duty_cycle = 65535

    def yellow(self):
        # The common anode RGB LED will glow yellow - set blue pin off and others on.
        self.r.duty_cycle = 0
        self.g.duty_cycle = 0
        self.b.duty_cycle = 65535

    def dark(self):
        # The common anode RGB LED will turn off
        self.r.duty_cycle = 65535
        self.g.duty_cycle = 65535
        self.b.duty_cycle = 65535

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

