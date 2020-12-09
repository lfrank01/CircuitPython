# Overview

For the Classes, Objects, and Modules assignment, libraries and classes were introduced. 

CircuitPython is an object-based programming language, meaning that individual objects or instances are created 
from libraries that contain the information for those objects. 

For example, consider the library `life`. In the `life` library, there could be a class called `Human`. 
In Circuit Python, the class `Human` would be referenced like this:

`from life import Human`

In the class `Human`, there would be different properties and methods. 
An object could be created from the class called "Luke."

Luke could have different properties such as age or hair color, and he could have methods such as eat or sleep.

This concept is the basis of object-based programming and is a super useful way of programming because it allows
similar information to be grouped into libraries and classes, making organization easier.

In the Classes, Objects, and Modules assignment, the code for a `main.py` file that made a common anode RGB 
LEDs change colors was given. The task was to create a library and class that made the code run properly.


# Lessons Learned 

* By convention, library names are not capitalized, such as `life`, and class names are capitalized, 
  such as `Human`.

* Every time an object is created, the class's `__init__` method is run by default. This means
  that code can be put in the `__init__` that is wanted to run for setting up an object. 
  For example, `me = Human("Luke")` takes the argument `Luke` and gives it to the class `Human` to 
  create a new Human object. The `__init__` method of `Human` would be run when this line is executed.

* An anode is a positively-charged electrode, and a cathode is a negatively-charged electrode.

* A common anode RGB LED is basically a red, green, and blue LED crammed into one compartment.

* The common anode RGB LED has an interesting way of being wired. A resistor must be placed between each RGB color leg 
  and its corresponding pin. This is because the RGB color legs run in parallel. Each RGB color leg requires a different 
  amount of voltage to operate (because of Physics) and if more than one were to be turned on, the voltage would default
  to the lowest voltage required, cutting off power from the other RGB legs. If only one RGB color leg was turned on, 
  one resistor could be shared among all of the RGB color legs, but it does not work when multiple are turned on.
  
* For a more in depth explanation, visit this site:
  [Common Anode RGB LED Wiring Explanation](https://www.circuitbread.com/tutorials/why-cant-i-share-a-resistor-on-the-common-anode-or-cathode-of-my-rgb-led)

* Also, here is my wiring diagram, though it was not hand-drawn because the wiring got messy:


More information is coming soon.

# On Using PyCharm As An IDE 
PyCharm is a free IDE (Integrated Development Environment) that makes software development easier.
Some of its functions include:
* Checking code for potential errors and providing code improvements.
* Compatibility with GitHub (Git pushes and Commits can be done directly)
* Spell-checking markdown files (.md).

To install PyCharm as a CircuitPython IDE, first, download PyCharm from `https://www.jetbrains.com/pycharm/download`
Afterward, follow the steps below:

1. Install the MicroPython plugin to PyCharm.

2. With the Metro Express attached, go to File > Settings > Languages & Frameworks > MicroPython. 
Enable it for this project and select device type "ESP8266". For device path, `COM5:` was used. This is the address
of the serial port the board used on **my** Windows computer. Other computers could be different.
   
This makes MicroPython appear in the PyCharm project navigation on the left under "External Libraries".

3. Go to File > Settings > Project > Project Structure. There, click "add content root" and navigate to the 
lib folder for the Adafruit Metro MO Express. 
   
This enables PyCharm to import the libraries and check usage of libraries against the library code.

It should be noted that some libraries like `board` and `neopixel` cannot be checked. They are
compiled into unreadable code (`.mpy`) that is specific to each CircuitPython type of board instead of Python, 
so PyCharm can't read them.
