import board
import time
from digitalio import DigitalInOut, Direction


class FancyLED:

    def __init__(self, pin1, pin2, pin3):
        led1 = DigitalInOut(pin1)
        led1.direction = Direction.OUTPUT
        led2 = DigitalInOut(pin2)
        led2.direction = Direction.OUTPUT
        led3 = DigitalInOut(pin3)
        led3.direction = Direction.OUTPUT
        # These variables don't need to be made into class variables with
        # a "self." because they don't need to be addressed by the class methods
        # individually - only as a collective. So the list that combines these
        # LED objects will need to be a class variable with "self."
        # Individual LEDs could however still be addressed by doing
        # self.led_list[0] which would be the 1st element in the list.
        # Note the square brackets to index a list, and that indexing starts
        # from 0.  The 1st element in a list is list[0].

        self.led_list = [led1, led2, led3]
        # An empty list is created by closed brackets [] and can be
        # added to by writing .append(something).
        self.all_off()  # start by explicitly turning all LEDs off.

    def alternate(self, number_of_blinks=4):
        # The method can be handed a variable for how many blinks we want, but it
        # has a default value for the variable so we don't have to give any variable.
        # It can also be left out when the method is called and it will work with the
        # default value.

        self.led_list[1] = True  # turn on the middle LED
        for blink_number in range(0, number_of_blinks):
            lit = False
            if blink_number % 2 == 0:
                lit = True
            # This line looks at the remainder of dividing blink_number by 2.
            # If this remainder is 0 (in other words, its an even number), the boolean variable
            # lit will be set to True
            # Another way of stating this would be:
            # lit = blink_number % 2 == 0
            self.led_list[0] = lit
            self.led_list[2] = not lit
            time.sleep(1)
        self.all_off()  # when blinking is finished, turn all of the LEDs off.

    def blink(self):

        self.all_off()  # when blinking is finished, turn all of the LEDs off.

    def chase(self):

        self.all_off()  # when blinking is finished, turn all of the LEDs off.

    def sparkle(self):

        self.all_off()  # when blinking is finished, turn all of the LEDs off.

    def all_off(self):
        for led in self.led_list:
            led = False
        # This loops through each LED in the list and sets it to False, turning it off.
