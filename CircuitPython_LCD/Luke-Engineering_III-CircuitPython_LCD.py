import time
import board
from lcd.lcd import LCD
import touchio
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
# NOTE I had to modify this library to 'import microcontroller'
# because the author had forgotten this.
# There is an issue about this mentioned on github but it hasnt yet been fixed:
# https://github.com/dhalbert/CircuitPython_LCD/issues

# OK. First, find out the address of my i2c board because
# apparently it is not the 0x27 default in the LCD library.
# This method of finding out the address I modified from:
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-i2c

i2c = board.I2C()
i2c.unlock()  # in case it was just used it needs to be unlocked

device_address = None

while not i2c.try_lock():
    pass

try:
    while not device_address:
        device_address_list = i2c.scan()
        # i2c.scan() returns a LIST of adddresses.
        # I just want the first address. So:
        device_address = device_address_list[0]
        print("I2C interface found at: ", hex(device_address))
        time.sleep(2)

finally:
    i2c.unlock()
    i2c.deinit()  # release the SCL pin so that the LCD can use it.
    # I found that here:
    # https://circuitpython.readthedocs.io/en/5.3.x/shared-bindings/busio/I2C.html#busio.I2C

# OK now talk to the lcd at the address we just found by scanning.
lcd = LCD(I2CPCF8574Interface(device_address), num_rows=2, num_cols=16)

lcd.clear()
lcd.print("Yo Luke \n")  # print \n means go to a new line
lcd.print("Ready?")
time.sleep(2)
lcd.clear()

# Read touched wires to count up or down.
touch_A3 = touchio.TouchIn(board.A3)
touch_A4 = touchio.TouchIn(board.A4)
count = 0

lcd.print("Count:" + str(count))

while True:
    # We need to clear the display every loop so that the text is replaced,
    # rather than added to previous text every time a wire is touched.

    if touch_A3.value and not touch_A4.value:
        lcd.clear()
        count = count + 1
        lcd.print("Count:" + str(count))

        while touch_A3.value:
            time.sleep(0.25)  # to 'debounce' the wire against multiple touches
            if touch_A4.value:
                break

    if touch_A4.value and not touch_A3.value:
        lcd.clear()
        count = count - 1
        lcd.print("Count:" + str(count))

        while touch_A4.value:
            time.sleep(0.25)  # debounce
            if touch_A3.value:
                break

    # When both wires are touched, we are done.
    if touch_A3.value and touch_A4.value:
        break

lcd.clear()
lcd.print("Bye")