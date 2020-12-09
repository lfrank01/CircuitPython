# This code was used to test if the common anode RGB LED was wired up correctly.

# It was a helpful way to test what was an input, what was an output, and to plan ahead for
# rest of the assignment.

import board
from digitalio import DigitalInOut, Direction, Pull

my_led = DigitalInOut(board.D3)
my_led.direction = Direction.OUTPUT

while True:
    my_led.value = False
