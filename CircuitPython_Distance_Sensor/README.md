# Overview
For the CircuitPython Distance Sensor assignment, the task was to wire up and code a HC-SR04 ultrasonic distance sensor to display the distance that it read through ultrasonic waves on the serial monitor. 

Furthermore, the code had to make the built-in neopixel on the Adafruit Metro MO Express change from red to pink to blue to light blue to green as the distance read went from 5 cm to 35 A range of 0 to 30 was not used because the HC-SRO4 has trouble reading distances between 0 and 5 cm, likley because the ultransonic waves bounce back before they are read. 

This assignment introudced a new library that was created for the HC-SR04. Here it is:
[adafruit_hcsr04.](https://github.com/adafruit/Adafruit_CircuitPython_HCSR04/blob/master/adafruit_hcsr04.py) file had to be added to the (.lib) folder of the CIRCUITPY removable USB!

The origonal ultrasonic distance sensor code that was built off of can be found here:
[Ultrasonic Sensor Base Code.](https://learn.adafruit.com/ultrasonic-sonar-distance-sensors/python-circuitpython)
# Lessons Learned

* A major takeaway from this assignment was the difference between different types of data values. The different types are a string (str), floating point number (float), and an integer (int).
  * The (str) stands for (string). It does not read numerical values but rather converts all of its data into a printable format. The (str) data type is required for (print) functions.
  *  The (float) stands for (floating point). It includes a demcial and any value, such as (8.) that includes a decimal will be considered a floating point number unless told otherwise.
  * The (int) stands for (integer). It is a whole number and it is important to note that it will always convert a decimal value whether it be greater than or less than (.5), to the first lowest integer. For example, (8.9) would become (8).



