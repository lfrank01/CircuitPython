# Hello CircuitPython
## Overview

The Hello CircuitPython assignment explained how to set up CircuitPython with my Metro Express. At the end of it, I was able to run my first code!

The proccess of setting up CircuitPython varies for different devices:

* For a Cromebook, use Caret for code and Beagle Term for a serial monitor.
* For a Mac or PC, use Mu. Mu incorporates code editing and a serial monitor.
* Keep in mind that for CircuitPython code editing, any text editor can be used. The file that the code is edited on will likley need a .py at the end of it to signify that it is CircuitPython.

After downloading Caret and Beagle Term on the Google Play Store for Chromebook, here is how I proceeded:

* Plug in the Metro Express. It should apear as a removable file. 
* In Caret, select the upload file option and find the Metro Express
* The screen should look like this:

![Metro Express Pop-Up](/Hello_CircuitPython/Luke-Engineering_III-Metro_Express_Pop_Up.png)

* Click on the main.py file. A .py file is CircuitPython.
* The file should have lots of text. If it is run, the Metro Express should perform something with the built in LED.

...

Here is my code. Note that code with a # is a comment and will not run:

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
