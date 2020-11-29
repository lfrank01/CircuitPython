# Overview
For the CircuitPython Distance Sensor assignment, the task was to wire up and code a HC-SR04 ultrasonic distance sensor to display on the serial monitor the distance that it read through ultrasonic waves. 

Furthermore, the code had to make the built-in neopixel on the Adafruit Metro MO Express change from red to pink to blue to light blue to green as the distance read went from 5 cm to 35. A range of 0 to 30 was not used because the HC-SRO4 had trouble reading distances between 0 and 5 cm, likley because the ultrasonic waves bounced back before they were read. 

This assignment introudced a new library that was created for the HC-SR04. Here it is:
[adafruit_hcsr04.](https://github.com/adafruit/Adafruit_CircuitPython_HCSR04/blob/master/adafruit_hcsr04.py) 

The origonal ultrasonic distance sensor code that was built off of can be found here:
[Ultrasonic Sensor Base Code.](https://learn.adafruit.com/ultrasonic-sonar-distance-sensors/python-circuitpython)

Two resistors came with the HC-SR04 ultrasonic distance sensor, but the component functioned without needing them. Apparently, digital IO pins have a logic level or power level of (3.3 V) and the power source that was used was (5.0 V), but the component functioned fine.

# Lessons Learned

* To highlight code in a markdown document, use a back quote- the key above (tab), not the one above (double quotes). This results in `code looking like this` instead of code looking like this. It's easier to see.

* Also, another markdown editing tip for emphasising words is to use an astrix before and after the word without any spaces seperating them. Intsead of something like (this), it looks something like *this*.

* A major takeaway from this assignment was the difference between different types of data values. The different types are a string `str`, floating point number `float`, and an integer `int`.

  * The `str` stands for (string). It does not read numerical values but rather converts all of its data into a printable format. The `str` data type is required for (print) functions.
  
  *  The `float` stands for (floating point). It includes a demcial and any value, such as (8.), that includes a decimal will be considered a floating point number unless told otherwise.
  
  * The `int` stands for (integer). It is a whole number and it is important to note that it will always convert a decimal value, whether it be greater than or less than (0.5), to the first lowest integer. For example, (8.9) would become (8). If we used a rounding function `round`, the result would be rounded to the nearest integer number instead of truncated - in this example, (9).
  
* By looking in the (adafruit_hcsr04) library, it became clear that the data type for the function `.distance` was a `float`. 

* For the `print` function, I had to convert the `float` into a `str` with code that looked like: 
`print("Distance is " + str(round(Distance)))`

* Now, for how an ultrasonic distance sensor works:
  * There are four pins, which are ground (GND), power (VCC), trigger pin (TRIG) and the echo pin (ECHO).
  
  * The trigger pin (TRIG) creates an ultrasonic pulse which travels out until hitting a solid which causes it to reflect back. It is the echo pin (ECHO) that recieves the reflected ultrasonic pulse and creates a readable output that is proportional to the time between when the ultrasonic pulse went out and came in.
  
* Here is an image explaning how the HC-SR04 and ultrasonic distance sensing work:

![Ultrasound explanation.](/CircuitPython_Distance_Sensor/Luke-Engineering_III-CircuitPython_Distance_Sensor-Ultrasound_Explanation.png)

#### Note - Work Cited for the website that I screenshoted this image from:
“How to Attach a HC-SR04 Ultrasonic Sensor (5v) to a Micro:Bit.” Teachwithict.com, www.teachwithict.com/hcsr045v.html. 
#### I used EasyBib for generating the MLA citation.

* My code comments explain most of how the code works. Here is a link to my code:
[CircuitPython_Distance_Sensor_Code.](/CircuitPython_Distance_Sensor/Luke-Engineering_III-CircuitPython_Distance_Sensor.py)

* Also, here is my hand-drawn circuit diagram:
[CircuitPython_Distance_Sensor_Circuit_Diagram.](Luke-Engineering_III-CircuitPython_Distance_Sesnor-Circuit_Diagram.pdf)

