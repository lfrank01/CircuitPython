# Overview

For the Classes, Objects, and Modules assignment, libraries and classes were introuded. 

More information is coming soon.

# Using PyCharm as an IDE
PyCharm is a free Integrated Development Environment that makes software development easier.
It helps with error checking and code consistency.
I downloaded it from `https://www.jetbrains.com/pycharm/download`, and then 
followed the following steps to enable PyCharm support for CircuitPython:

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

* By convention, class names are capitalized, such as `class Dog`.

* Classes include shared variables and methods. Objects are what get created when we make separate instances of a class.

* Every time an object is created, the class's `__init__` method is run by default. This means
we can put code in `__init__` that we want to run for setting up an object according to
  any arguments that were given to the class when we created it. For example, `me = Human("Luke")`
  takes the argument `Luke` and gives it to the class `Human` to create a new Human object.
  The `__init__` method of `Human` would be run when this line is executed.
  

More information is coming soon.
