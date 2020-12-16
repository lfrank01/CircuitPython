import time
import random
from digitalio import DigitalInOut, Direction


class FancyLED:
    def __init__(self, a_pin, b_pin, c_pin):

        led1 = DigitalInOut(a_pin)
        led1.direction = Direction.OUTPUT

        led2 = DigitalInOut(b_pin)
        led2.direction = Direction.OUTPUT

        led3 = DigitalInOut(c_pin)
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

        print("Alternating now")
        self.led_list[1].value = True  # turn on the middle LED

        for blink_number in range(0, number_of_blinks):
            lit = False
            if blink_number % 2 == 0:
                lit = True
            # This line looks at the remainder of dividing blink_number by 2.
            # If this remainder is 0 (in other words, its an even number), the boolean variable
            # lit will be set to True
            # Another way of stating this would be:
            # lit = blink_number % 2 == 0
            self.led_list[0].value = lit
            self.led_list[2].value = not lit
            time.sleep(1)
            print(str(blink_number))

    def blink(self, number_of_blinks=6):

        print("Blinking now")
        for blink_number in range(0, number_of_blinks):
            lit = False

            if blink_number % 2 == 0:
                lit = True

            self.led_list[0].value = lit
            self.led_list[1].value = lit
            self.led_list[2].value = lit
            time.sleep(1)

            print(str(blink_number))

    def chase(self, number_of_chases=4):

        print("Chasing now")
        counter = 0
        for blink_number in range(0, number_of_chases):
            lit = False

            if counter == 0:
                self.led_list[0].value = not lit
                self.led_list[1].value = lit
                self.led_list[2].value = lit
                counter += 1
                print("Counter:" + str(counter))
                time.sleep(1)

            if counter == 1:
                self.led_list[0].value = not lit
                self.led_list[1].value = not lit
                self.led_list[2].value = lit
                counter += 1
                print("Counter:" + str(counter))
                time.sleep(1)

            if counter == 2:
                self.led_list[0].value = not lit
                self.led_list[1].value = not lit
                self.led_list[2].value = not lit
                counter = 0
                print("Counter:" + str(counter))
                time.sleep(1)

    def sparkle(self, number_of_sparkles=50):

        print("Sparkling now")
        lit = True
        for blink_number in range(0, number_of_sparkles):
            self.led_list[0].value = not lit
            self.led_list[1].value = not lit
            self.led_list[2].value = not lit

            self.led_list[random.randrange(0, 3, 1)].value = lit
            time.sleep(0.1)

    def all_off(self):

        for led in self.led_list:
            led.value = False
        time.sleep(1)
        # This loops through each LED in the list and sets it to False, turning it off.

# For nicer looking code, I used a tool called "black": https://pypi.org/project/black/
# It reformats any python file into a standard format. To use it you open a terminal window in
# the same directory as the file and enter for example: black fancyLED.py
