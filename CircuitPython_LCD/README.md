# CircuitPython_LCD

## Overview

For the CircuitPython LCD assignment, there were several subtle parts that made the creation of the code difficult. Luckily, I had the help of my father, who happens to be a computer programmer. The goal of the assignment was to wire up an LCD so that when one button was pressed, a counter would move up by one, and when another button was pressed, the counter would move down by one.

In order to accomplish this, there was a repository that contained LCD code suited for Metro Express and another repository that contained code to update the adafruit_bus_library. In this repository, there was a file named "i2c_pcf8574_interface.py." This file was missing an "import microcontroller," and one of the reasons that the code was not working was because of that. That file is updated in [my repository.](https://github.com/lfrank01/CircuitPython/blob/main/CircuitPython_LCD/i2c_pcf8574_interface.py)

The website [CircuiPython Read The Docs](https://readthedocs.org/projects/circuitpython/) was a helpful tool, as it allowed me to search for the libraries that were needed.

Another reason that the code was not working could have been because the Metro MO Express did not have enough space. In the serial monitor, there would have likely been a message saying "memory allocation error." In order to solve this, Dr. Shields translated the (.py) files from the LCD repository into (.mpy) files. The (.mpy) file translates standard python code into micropython code, which compresses the data. In order to do this, there is a .mpy cross programm, though it is only available for Linux.


## Lessons Learned

Lessons Learned will be updated shortly. More content is coming.

* Most of my lessons learned are in my code, here:

![CircuitPython_LCD_Code](/CircuitPython_LCD/Luke-Engineering_III-CircuitPython_LCD.py)

* Here is my hand-drawn circuit diagram:

![CicuitPython_LCD_Circuit_Diagram](/CircuitPython_LCD/Luke-Engineering_III-CircuitPython_LCD_Circuit_Diagram.pdf)

