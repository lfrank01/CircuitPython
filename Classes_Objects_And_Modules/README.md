# Overview

For the Classes, Objects, and Modules assignment, libraries and classes were introduced. 

More information is coming soon.

# Lessons Learned 

* It is better not to use commas in naming, like for Classes, Objects, And Modules, because some programs may see commas as a reference to something or formatting change.

* Class names are capitalized, such as `class Dog`, but library names are not. An example of this would be `from dog import Dog`

* Classes include shared variables and methods. Methods distinguish seperate instances of a class. 

More information is coming soon.

# Notes:

* The Adafruit Metro MO Express shoukd be plugged into the computer before starting up PyCharm. Otherwise, PyCharm will think the (lib) added-on library has no destination, and it will ignore it.

* Steps:
  * Made a new `.main` file called `TestLed.py` and imported board and digitalio.
  * Made test code to get one RGB color working in the `main.py` file:
   `import board`
   `from digitalio import DigitalInOut, Direction, Pull
   `my_led = DigitalInOut(board.D3)
   `my_led = Direction.OUTPUT`
   
   `while True`
    `my_led = value.False`
    
 * I needed to have a self in `self.r.value = False or True`.
 
 * Edit > Find > Replace for replacing information on PyCharm.
   
