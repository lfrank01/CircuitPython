import time
import board
from lcd.lcd import LCD
import touchio
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
# NOTE - I had to modify this library to 'import microcontroller'...
# ...because the author had forgotten to.
# There is an issue about this mentioned on github but it hasn't yet been fixed:
# https://github.com/dhalbert/CircuitPython_LCD/issues.

# OK. First, find out the address of my i2c board because...
# apparently it is not the 0x27 default in the LCD library.
# This method of finding out the address I modified from:
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-i2c.

i2c = board.I2C()
i2c.unlock()  # In case it was the i2c was just used, it needs to be unlocked.

device_address = None

while not i2c.try_lock():
    pass  # I do not know how to explain this.

try:
    while not device_address:
        device_address_list = i2c.scan()
        # The i2c.scan() returns a LIST of addresses.
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

lcd.clear()
lcd.print("Yo Luke \n")  # Print \n means "go to a new row on the LCD screen."
lcd.print("Ready?")
time.sleep(2)
lcd.clear()

# Pins A3 and A4 are used as capacitive touch wires to count up or down.
touch_A3 = touchio.TouchIn(board.A3)
touch_A4 = touchio.TouchIn(board.A4)
count = 0  # Count is set at zero to begin with.

lcd.print("Count:" + str(count))
# The "Count:" is a series of letter that will show on the LCD screen.
# The str(count) takes whatever the value the variable  "count" is...
# ...and shows it on the LCD screen.

while True:

    if touch_A3.value and not touch_A4.value:
        # Note - This code ensures that touch_A3.value will not...
        # ...run at the same time at touch_A4.value.
        lcd.clear()
        count = count + 1
        lcd.print("Count:" + str(count))

        while touch_A3.value:
            time.sleep(0.25)
            # This code 'debounces' the wire against multiple touches.
            if touch_A4.value:
                break
                # The "break" end the while loop, which ends by...
                # ...touch_A4.value or touch_A4.value and touch_A3.value.

    if touch_A4.value and not touch_A3.value:
        lcd.clear()
        count = count - 1
        lcd.print("Count:" + str(count))

        while touch_A4.value:
            time.sleep(0.25)
            if touch_A3.value:
                break

    if touch_A3.value and touch_A4.value:
        break
        # When both wires are touched, the while True loop ends.

lcd.clear()
lcd.print("Bye!")
# The LCD clears and prints a farewell message.
