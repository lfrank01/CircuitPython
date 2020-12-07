# Overview

For the Classes, Objects, and Modules assignment, libraries and classes were introuded. 

More information is coming soon.

# Using PyCharm as an IDE
I followed the following steps to enable PyCharm support for CircuitPython:

1. Install the MicroPython plugin to PyCharm

2. With the Metro Express attached, go to File > Settings > Languages & Frameworks > MicroPython. 
I enabled it for this project and selected device type "ESP8266". For device path, I entered `COM5:`. This is the address
of the serial port the board used on my Windows computer. Other computers could be different.
This makes MicroPython appear in the PyCharm project navigation on the left under "External Libraries".

3. I went to File > Settings > Project > Project Structure. There I clicked "add content root", and navigated to the 
lib folder on my Metro Express. This enables PyCharm to import the
libraries and check my usage of libraries against the library code.

I should note that some libraries like `board` and `neopixel` cannot be checked, because they are
compiled into unreadable code specific to each CircuitPython type of board rather than being in Python, so PyCharm can't
read them.


 


# Lessons Learned 

* Class names are capitalized, such as /class Dog/.

* Classes include shared variables and methods. Methods distinguish seperate instances of a class. 

More information is coming soon.
