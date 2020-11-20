# Overview
For the CircuitPython_Photointerrupter assignment, I had to wire up and code a photointerrupter to emmit the number of times it had been interrupted every four seconds. An LCD add-on for displaying the number of interruptions was optional. I might add that onto my code.

Also, I used the "T-shaped, slot center 7mm" model for my photointerrupter. The different variations can be found [here.](https://cdn-shop.adafruit.com/product-files/3986/ee-sx47_67_ds_e_13_2_csm483.pdf)

#### Note - A key takeaway was that there is lots of great information online, but the value of the information lies in understanding it, not just copying and pasting it. I was puzzled by this assignment origonally, so I copied and pasted some code from [another repository](https://github.com/gventre04/CircuitPython/blob/master/photointerrupter.py) onto the (main.py) file and ran it. It worked, but I didn't understand why. I commented the parts of the code that confused me and tried tampering with the code to understand it better.

## Lessons Learned
* (HIGH) in C++ is (True) in CircuitPython; (LOW) in C++ is (False) in CircuitPython.

* My photointerrupter had three wires: (VCC), (GND), and a pin wire. The pin wire went to a Digital IO Pin, which means input/output.

* The photointerrupter read either (True), wiring to (VCC), or (False), wiring to (GND). The question was "which is the default?"

* That's where (Interrupter.pull = Pull.UP), mentioned earlier in the code with (from digitalio import DigitalInOut, Direction, Pull), comes into play. It pulls up a resistor and makes the default reading (True) or to (VCC).

* For more information, look at the image below. Pretend that the button is the photointerrupter:

![Pulled-Up_Resistor_Picture](/CircuitPython_Photointerrupter/Luke-Engineering-III-CircuitPython_Photointerrupter-PulledUp_Resistor)

* I learned about the (digitalio) and (time) repositories: 
  * The (digitalio) repository is used for controlling digital input/output pins. I used it for the pin pull-up command.
  * The (time) repository does, well, time. I have used it before in cases such as (time.sleep). I used it in this code for (time.time), which is a clock that counts in seconds. It was used to time the interval between each serial monitor message and allowed me to have the time counted in integers.

* My code comments explain most of how the code works. Here is a link to my code:
[CircuitPython_Photointerrupter_Code.](/CircuitPython_Photointerrupter/Luke-Engineering_III-CircuitPython_Photointerrupter.py)

* Also, here is my hand-drawn circuit diagram:
[CicuitPython_Photointerrupter_Circuit_Diagram.](/CircuitPython_Photointerrupter/Luke-Engineering_III-CircuitPython_Photointerrupter_Circuit_Diagram.pdf)
