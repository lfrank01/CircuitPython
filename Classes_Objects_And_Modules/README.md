# Overview

For the Classes, Objects, and Modules assignment, libraries and classes were introduced. 

CircuitPython is an object-based programming language, meaning that individual objects or instances are created 
from libraries that contain the information for those objects. 

For example, consider the library `life`. In the `life` library, there could be a class called `Human`. 
In Circuit Python, the class `Human` would be referenced like this:

`from life import Human`

The code for the library `life` would usually be placed in a file called `life.py`.

In the class `Human`, there would be different properties and methods. 
An object called "Luke" could be created from the class `Human.`

`Luke` could have different properties such as age or hair color, and he could have methods such as eat or sleep.

This concept is the basis of object-based programming and is a super useful way of programming because it allows
similar information to be grouped into libraries and classes, making organization easier.

In the Classes, Objects, and Modules assignment, the code for a `main.py` file was given that made a common-anode RGB 
LEDs change colors. The task was to create a library and class that made the code run properly. As an add-on, a function 
for fading through colors, and a function for randomly selecting color "positives" and "negatives" were created.


# Lessons Learned 

* By convention, library names are not capitalized, such as `life`, and class names are capitalized, 
  such as `Human`.

* Every time an object is created, the class's `__init__` method is run by default. This means
  that code can be put in the `__init__` that is wanted to run for setting up an object. 
  For example, `me = Human("Luke")` takes the argument `Luke` and gives it to the class `Human` to 
  create a new Human object. The `__init__` method of `Human` would be run when this line is executed.

* An anode is the negatively-charged electrode of the LED (where electrons flow out), and a cathode is the positively-charged electode of the LED 
  (where electrons flow in).

* A common-anode RGB LED is basically a red, green, and blue LED crammed into one compartment. Electrons flow into 
  one of the pins corresponding to a color, and they all flow out of the common-anode pin back to the power source 
  (to the positive connection because electrons are attracted to positive charge and repelled by negative charge).

* The common-anode RGB LED has an interesting way of being wired. A resistor must be placed between each RGB color leg 
  and its corresponding pin. This is because the RGB color legs run in parallel. Each RGB color leg requires a different 
  amount of voltage to operate (because of Physics) and if more than one were to be turned on, the voltage would default
  to the lowest voltage required, cutting off power from the other RGB legs. If only one RGB color leg was turned on, 
  one resistor could be shared among all the RGB color legs, but it does not work when multiple are turned on.
  
* For a more in depth explanation, visit this site:
  [Common Anode RGB LED Wiring Explanation](https://www.circuitbread.com/tutorials/why-cant-i-share-a-resistor-on-the-common-anode-or-cathode-of-my-rgb-led)
  
* Also, it is important to note that the common-anode leg will be the longest leg in the common-anode RGB LED.
  Then, the leg to the right is the red RGB color leg.
  
* Here is a wiring diagram, though it was not hand-drawn because the wiring got messy:
![Two Common Anode RGB LEDs Circuit Diagram](/Classes_Objects_And_Modules/Two_Common_Anode_RGB_LEDs.png)

#### Note - The circuit diagram was made on Tinkercad, which does not have an Adafruit Metro MO Express import option. The circuit diagram might be changed another time if a better circuit diagram creator if found.

* Another helpful tip was to create some test code to check how the common-anode RGB LED worked. 

* Here is what was used for the test code:
[Test_LED.py](/Classes_Objects_And_Modules/Test_Led.py)
  
* My code comments explain most of how the code works. Here is my library code that uses pulse-width modulation:
[rgb_pwm.py](/Classes_Objects_And_Modules/rgb_pwm.py)
  
* Additionally, here is the digital input-output code. However, this code is not used in the main.py file because 
  it cannot make as many colors as PWM can:
[rgb.py](/Classes_Objects_And_Modules/rgb.py)
  
* Below is the `main.py` file that imported the `rgb.py` library:
[main.py](/Classes_Objects_And_Modules/main.py)

**Note on using digital outputs**

* The assignment called for the use of digital outputs to drive the common-anode RGB LEDs, not analog ones. 
  As a result, the color possibilities were limited to combinations of the pins being either on (False) or off (True). 
  This would result in 8 possible colors being rendered, including black (all off) and 
  white (all on). There were (2^3) combinations for colors because there were 3 pins and 2 states.

* The library `digitalio` was used to drive the digital output pins. To make more colors, one would have to use 
  pulse-width modulation (PWM) on the digital output pins to create the effect of analog variation. 
  Analog variation would control the current flowing to each pin rather than the digital states being limited 
  to on or off, creating more possible color options.

**Note on using pulse-width modulation (PWM)**

A bonus for this assignment was to create a rainbow function that made a common-anode RGB LED cycle through the 
colors of the rainbow. Pulse-width modulation was required for the rainbow function, since the colors orange, indigo,
and violet cannot be made by just turning colors on and off. Below are some lessons learned about pulse-width modulation:

* To vary the common-anode RGB LEDs, pulse-width modulation uses frequency and duty cycle.

* For more information on frequency and duty cycle, here is an [explanation](https://github.com/lfrank01/CircuitPython/tree/main/CircuitPython_Servo)
  from a previous assignment. To summarize the explanation, the frequency is how many times in a selected period of time
  that the reading will vary between on and off. Then, duty cycle is the ratio between when the reading is on and off. 
  Basically, the duty cycle controls the duration of when the frequency is high.
  
* The digital input-outputs pins on the Adafruit Metro MO Express are 1, 2, 3, 4, 5, 7, 9, 11, 12, and 13.

* If the digital input-output pins 0, 6, 8, and 10 are used, the error "All timers in use" will appear. 

* The frequency controls how many times per second the common-anode RGB LED will refresh. It is advisable to keep the 
  frequency below 50 because, after a frequency of 24 (what movies use), the change in frequency is not visible to the 
  human eye.


# On Using PyCharm As An IDE 
PyCharm is a free IDE (Integrated Development Environment) that makes software development easier.
Some of its functions include:
* Checking code for potential errors and providing code improvements.
* Compatibility with GitHub (Git pushes and commits can be done directly)
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
