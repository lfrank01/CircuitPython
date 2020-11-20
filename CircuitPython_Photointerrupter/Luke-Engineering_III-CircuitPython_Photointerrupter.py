# Origonal code is from:
# https://github.com/gventre04/CircuitPython/blob/master/photointerrupter.py

from digitalio import DigitalInOut, Direction, Pull
# It did not recognize the (Direction) parameter, so it had to be included.
# (DigitalInOut) is a pin in the class (digitalio) used to control I/O pins.
# (direction) is a parameter of (DigitalInOut),...
# ... change a pin between an input and output.

import time  # Used in start = time.time.
import board
# (Remaining = max - time.time()) was undefined, so I looked up the (max)
Interrupter = DigitalInOut(board.D7)
# Created a variable for the interrupter.
# D7 is an I/O (Input/Output) pin.

Interrupter.direction = Direction.INPUT
# By using the direction parameter, I choose whether the pin...
# ... is an input or output. I made it an input.

Interrupter.pull = Pull.UP
# For data on what a pull-up resistor is, I went to:
# https://learn.sparkfun.com/tutorials/pull-up-resistors/all

# Without a pin push or pull hen a microcontroller is connected to a pin,...
# ... it is hard to tell if the pin is HIGH (VCC) or LOW (GND).

# With a pull-up resistor, the photointerrupter reads...
# ... high when it is not acitve.

# When the photointerruptor is activated,...
# ... it reads as LOW and connects to ground.

Photo = False

State = False

Counter = 0

max = 4

Start = time.time()  # What is (Start)?

while True:
    State = Photo
    Photo = Interrupter.value
    # (.value) is the "digital logic level of the pin."
    if Photo and not State:
            Counter += 1

    Remaining = max - time.time()

    if Remaining <= 0:
        print("Interrupts:", str(Counter))
        max = time.time() + 4
        Counter = 0