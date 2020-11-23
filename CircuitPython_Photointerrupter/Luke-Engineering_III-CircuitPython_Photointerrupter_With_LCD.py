# Origonal code is from:
# https://github.com/gventre04/CircuitPython/blob/master/photointerrupter.py

# This code includes LCD usage.
from digitalio import DigitalInOut, Direction, Pull
# It did not recognize the (Direction) parameter, so it had to be included.

# (DigitalInOut) is a parameter in the class (digitalio)...
# ... used to control I/O pins.

# (direction) is a parameter of (DigitalInOut),...
# ... change a pin between an input and output.

import time  # Used in start = time.time.
import board

# -------------- LCD Setup Start --------------

from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import LCD

i2c = board.I2C()
i2c.unlock()  # In case it was the i2c was just used, it needs to be unlocked.

device_address = None

while not i2c.try_lock():
    pass  # I do not know how to explain this.

try:
    while not device_address:
        device_address_list = i2c.scan()
        # The i2c.scan() returns a LIST of adddresses.
        # I just want the first address. So:
        device_address = device_address_list[0]
        print("I2C interface found at: ", hex(device_address))
        time.sleep(2)

finally:
    i2c.unlock()
    i2c.deinit()
    # This releases the SCL (Serial Clock Wire) pin so that the LCD can use it.
    # I found that here:
    # https://circuitpython.readthedocs.io/en/5.3.x/shared-bindings/busio/I2C.html#busio.I2C

# OK, now talk to the LCD at the address we just found by scanning.
lcd = LCD(I2CPCF8574Interface(device_address), num_rows=2, num_cols=16)

# -------------- LCD Setup End  --------------

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

lcd.print("LCD Go.")

time.sleep(2)  # Looking for alternative for time.sleep.

lcd.clear()

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
        lcd.clear()
        print("Interrupts:" + str(Counter))
        lcd.print("Breaks:" + str(Counter))

        # The use of a comma between "Breaks" and str(counter) is required...
        # ... because a standard print statement will only take one argument.
        # The error message was:
        # "function takes 2 positional arguments but 3 were given."
        # This was because I used a (,), which seperates arguments.
        # The (+) makes the two arguments into one, allowing the code to work.

        Max = time.time() + 4

        # There is a case when multiple argument...
        # ... can be given: inline formatting.
        # Inline formatting looks something like this:
        # print("Interrupts: %i, mood: %s, moonphase: %d", Counter)
        # The %s are fillers for the strings and the commas seperate them.
        # The (%i) would indictate an integer.
