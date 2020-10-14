import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:

    print("Blue")

    dot.fill((0,0,100))

    time.sleep(1)

    # The number in parentheses represents seconds. In C++, it represented milliseconds. To shorten the time, create a decimal such as (0.5)

    print("Green")

    dot.fill((0,100,0))

    #Two sets of parentheses are needed to make the RGB function work. When one set of parentheses was used, it did not work.

    time.sleep(1)

    print("Red")

    # Only one set of parentheses needed, but quotation marks must be included for the print function to work.

    dot.fill((100,0,0))

    time.sleep(1)

    # (cntrl) + (d) resets the terminal screen for Beagle Term. It is helpful if the terminal is loaded with text. It does not work if functional code is running; at least, that is what it seems like.
