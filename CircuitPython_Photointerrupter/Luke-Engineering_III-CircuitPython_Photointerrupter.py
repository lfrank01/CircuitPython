# Origonal code is from:
# https://github.com/gventre04/CircuitPython/blob/master/photointerrupter.py

from digitalio import DigitalInOut, Direction, Pull
# It did not recognize the (Direction) parameter, so it had to be included.

# (DigitalInOut) is a parameter in the class (digitalio)...
# ... used to control I/O pins.

# (direction) is a parameter of (DigitalInOut),...
# ... change a pin between an input and output.

import time  # Used in start = time.time.
import board

Interrupter = DigitalInOut(board.D7)
# Created a variable for the interrupter.
# D7 is an I/O (Input/Output) pin.

Interrupter.direction = Direction.INPUT
# By using the direction parameter, I choose whether the pin...
# ... is an input or output. I made it an input.

Interrupter.pull = Pull.UP
# For data on what a pull-up resistor is, I went to:
# https://learn.sparkfun.com/tutorials/pull-up-resistors/all

# Without a pin push or pull pin, when a microcontroller is connected...
# ... to a pin it is hard to tell if the pin is True (VCC) or False (GND).

# With a pull-up resistor, the photointerrupter reads...
# ... high when it is not acitve.

# When the photointerruptor is activated,...
# ... it reads as (False) and connects to ground.

Photo = True
# These could also both be False, just as long as they are the same.

State = True
# For data on loops and conditions such as (False):
# http://projectpython.net/chapter03/

Counter = 0

Max = 4

while True:

    State = Photo
    Photo = Interrupter.value
    # If line 46 and 45 switch, the code doesn't work.

    # (.value) is the "digital logic level of the pin,"...
    # ... Meaning whether it is HIGH or LOW.

    if Photo and not State:
            Counter += 1

    Remaining = Max - time.time()

    if Remaining <= 0:  # (==) does not work.
        print("Interrupts:" + str(Counter)) # A (,) would not work.
        Max = time.time() + 4
