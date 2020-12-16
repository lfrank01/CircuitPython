import time
import random
from digitalio import DigitalInOut, Direction


class FancyLED:
    def __init__(self, pin1, pin2, pin3):

        led1 = DigitalInOut(pin1)
        led1.direction = Direction.OUTPUT

        led2 = DigitalInOut(pin2)
        led2.direction = Direction.OUTPUT

        led3 = DigitalInOut(pin3)
        led3.direction = Direction.OUTPUT

        # The variables led1, led2, and led3 do not need a "self" statement because they are addressed in the
        # the list below.

        self.led_list = [led1, led2, led3]

        # Each LED variable does not each need a self statement individually. Instead, The LED variables are given
        # the self statement as a collective in the list.

        # Individual LEDs can be addressed by writing self.led_list[number] which would take the specified LED in
        # the list for use. Multiple LEDs can also be addressed by writing self.led_list[number, number, etc.].

        # It is important to note that the square brackets [] will index a list. Oddly enough, the indexing starts at
        # 0. For example, self.led_list[0] would refer to the first item in the list, and self.led_list[1] would refer
        # to the second.

        # Additionally, an empty list is created with closed, empty brackets []. An empty list can be added to by
        # writing something similar to "list.append(something)."

        self.all_off()
        # Begin by explicitly turning all LEDs off.
        # The "all_off" method was an additional method created for convenience that was not listed in the assignment.

    def alternate(self, number_of_alternates=4):
        # The method "alternate" can be assigned a variable for how many times it should blink.
        # In this case, the code is setting 4 as the default value for number_of_blinks, but it can be changed.

        # In the main.py file, if an object used the method by object.alternate(), the default value would be 4.

        print("Alternating now")

        self.led_list[1].value = True
        # The middle LED is turned on for the alternating process.

        for alternate_number in range(0, number_of_alternates):
            # The "range" method is a handy tool for specifying the number of times that code should repeat.
            # In this case, the code will by default repeat 4 times because it goes from 0 -> 1 -> 2 -> 3.
            # When using "range," CircuitPython starts from 0 and go to one less than the maximum value listed.

            lit = False

            if alternate_number % 2 == 0:
                lit = True

            # Using "%2" divides the blink_number by 2 and then looks at the remainder.

            # If this remainder is 0 (in other words, an even number), the boolean variable "lit" will be set to True.
            # Otherwise, the boolean variable "lit" is set to False.

            # Additionally, "if blink_number % 2 == 0: lit = True" could be writen as "lit = blink_number % 2 == 0."

            self.led_list[0].value = lit
            self.led_list[2].value = not lit
            # This code alternates the far left and far right LED between on and off, creating an alternating effect.
            time.sleep(1)
            print("Alternate Counter: " + str(alternate_number) + " out of " + str(number_of_alternates))

    def blink(self, number_of_blinks=6):
        # LEDs in object will blink on and off.

        print("Blinking now")

        for blink_number in range(0, number_of_blinks):
            lit = False

            if blink_number % 2 == 0:
                lit = True

            self.led_list[0].value = lit
            self.led_list[1].value = lit
            self.led_list[2].value = lit
            time.sleep(1)

            print("Blink Counter: " + str(blink_number) + " out of " + str(number_of_blinks))

    def chase(self, number_of_chases=4):
        # LEDs in object will one by one all turn on.

        print("Chasing now")
        counter = 0
        for chase_number in range(0, number_of_chases):
            lit = False

            if counter == 0:
                self.led_list[0].value = not lit
                self.led_list[1].value = lit
                self.led_list[2].value = lit
                counter += 1
                # print("Chase Counter: " + str(counter))
                time.sleep(1)

            if counter == 1:
                self.led_list[0].value = not lit
                self.led_list[1].value = not lit
                self.led_list[2].value = lit
                counter += 1
                # print("Counter: " + str(counter))
                time.sleep(1)

            if counter == 2:
                self.led_list[0].value = not lit
                self.led_list[1].value = not lit
                self.led_list[2].value = not lit
                counter = 0
                # print("Counter: " + str(counter))
                time.sleep(1)

    def sparkle(self, number_of_sparkles=50):
        # LEDs will randomly blink on and off.

        print("Sparkling now")
        lit = True
        for sparkle_number in range(0, number_of_sparkles):
            self.led_list[0].value = not lit
            self.led_list[1].value = not lit
            self.led_list[2].value = not lit

            self.led_list[random.randrange(0, 3, 1)].value = lit

            # To generate random numbers, the randrange method was used from the "random" library. A similar bit of code
            # could be used to generate random methods. To do so, the methods would have to be included in a list. From
            # there, the randrange method could pick out random methods in the list.

            # For more information on the "random library," here is Adafruit CircuitPython Read the Docs (5.3):
            # https://circuitpython.readthedocs.io/en/2.x/shared-bindings/random/__init__.html

            time.sleep(0.1)
            # print("Sparkle Counter:" + str(sparkle_number) + "out of" + str(number_of_sparkles))
            # Printing the sparkle counter crowds the serial monitor, but it can be used.

    def all_off(self):

        for led in self.led_list:
            led.value = False
        time.sleep(1)
        # This loops through each LED in the list and sets it to False, turning it off.

# Note - For code formatting, the tool called "black" was helpful. Black will reformat any python file into a standard
# format. To use it, open a terminal window in the same directory as the file and enter for example: black fancyLED.py

# Here it the link to black:
# https://pypi.org/project/black/
