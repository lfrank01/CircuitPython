# Overview
For the CircuitPython_Photointerrupter assignment, I had to wire up and code a photointerrupter to emmit the number of times it had been interrupted every four seconds. Additionally, I created code that allowed an LCD to display the number of interrupts every four seconds.

I used the "T-shaped, slot center 7mm" model for my photointerrupter. The different variations can be found [here.](https://cdn-shop.adafruit.com/product-files/3986/ee-sx47_67_ds_e_13_2_csm483.pdf)

#### Note - A key takeaway was that there is a lot of great information online, but the value of the information lies in understanding it, not just copying and pasting it. I was puzzled by this assignment origonally, so I copied and pasted some code from [another repository](https://github.com/gventre04/CircuitPython/blob/master/photointerrupter.py) onto the (main.py) file and ran it. It worked, but I didn't understand why. I commented the parts of the code that confused me and tried messing with the code to understand it better.

## Lessons Learned
* (HIGH) in C++ means (True) in CircuitPython; (LOW) in C++ means (False) in CircuitPython.

* My photointerrupter had three wires: (VCC), (GND), and a pin wire. The pin wire went to a Digital IO Pin, which means input/output.

* The photointerrupter read either (True), wiring to (VCC), or (False), wiring to (GND). The question was "Which is the default?"

* That's where (Interrupter.pull = Pull.UP), mentioned earlier in the code with (from digitalio import DigitalInOut, Direction, Pull), comes into play. It pulls up a resistor and makes the default reading (True) or to (VCC).

* For more information, look at the image below. Pretend that the button is the photointerrupter:

![Pulled-Up_Resistor_Picture](/CircuitPython_Photointerrupter/Luke-Engineering-III-CircuitPython_Photointerrupter-PulledUp_Resistor.png)

#### Note - Work Cited for the website that I screenshoted this image from:
Pull-up Resistors, www.learn.sparkfun.com/tutorials/pull-up-resistors/all. 
#### I used EasyBib for generating the MLA citation.

* I learned about the (digitalio) and (time) repositories: 
  * The (digitalio) repository is used for controlling digital input/output pins. I used it for the pin pull-up command.
  * The (time) repository does, well, time. I have used it before in cases such as (time.sleep). I used it in this code for (time.time), which is a clock that counts in seconds. It was used to time the interval between each serial monitor message and allowed me to have the time counted by integers.

* My code comments explain most of how the code works. Here is a link to my code:
[CircuitPython_Photointerrupter_Code.](/CircuitPython_Photointerrupter/Luke-Engineering_III-CircuitPython_Photointerrupter.py)

* Also, here is my hand-drawn circuit diagram:
[CicuitPython_Photointerrupter_Circuit_Diagram.](/CircuitPython_Photointerrupter/Luke-Engineering_III-CircuitPython_Photointerrupter-Circuit-Diagram.pdf)

#### I also have code with an LCD add-on.
[CircuitPython_Photointerrupter_Code With An LCD.](/CircuitPython_Photointerrupter/Luke-Engineering_III-CircuitPython_Photointerrupter_With_LCD.py)

* From this code, I learned that a standard (print) or (lcd.print) command will only take one argument. 
* Functional code would look like (lcd.print("Interrupts:" + str(Counter)), not (lcd.print("Interrupts:" , str(Counter)).
* A comma seperates arguments, so it would not work in these code statements.
* There are ways to include multiple arguments in a print statement. For a brief example, look at the code comments at the bottom of the LCD add-on code.
* Another lesson learned was that I had to wire up two components to 5V. A simple but subtle solution was to connect power to the breadboard, and from there, connect my components to power. Mismatching power inputs and outputs can lead to malfunctions. Also, Vin is not intended for power supply; it is used to power the Adafruit Metro MO Express if needed, not for the Adafruit Metro MO Express to power other components.
#### Here is my circuit diagram for an LCD with photointerrupter:
[CicuitPython_Photointerrupter_Circuit_Diagram With LCD.](/CircuitPython_Photointerrupter/Luke-Engineering_III-CircuitPython_Photointerrupter-Circuit_Diagram_With_LCD.pdf)
