# CircuitPython_LCD

## Overview

For the CircuitPython LCD assignment, there were several subtle parts that made the creation of the code difficult. Luckily, I had the help of my father, who happens to be a computer programmer. The goal of the assignment was to wire up an LCD so that when one wire was pressed, a counter would move up by one, and when another wire was pressed, the counter would move down by one. Furthermore, the counter was supposed to only go up after each press, and not continue to go up when holding down a wire.

In order to accomplish this, there was a repository that contained LCD code suited for Metro Express and another repository that contained code to update the adafruit_bus_library. In the LCD repository, there was a file named "i2c_pcf8574_interface.py," which made the LCD backpack work. A key note was that the author of the file used a microcontroller library instead of time.sleep(), because it was more accurate; except, he forgot to include an import of the microcontroller library in his code, so the code did not work.

That file is updated in [my repository.](https://github.com/lfrank01/CircuitPython/blob/main/CircuitPython_LCD/i2c_pcf8574_interface.py)

The website [CircuiPython Read The Docs](https://readthedocs.org/projects/circuitpython/) was a helpful tool, as it allowed me to search for the libraries that were needed.

Another note was that the Metro MO Express may not have had the memory to run the i2c code, among other large libraries such as capacitive touch. As a solution, Dr. Shields converted the (.py) libraries into (.mpy) files, which are compressed. This was a smart decision. However, I did not do it, because an (.mpy) file is not readable, and I wanted to be able to understand the libraries.

## Lessons Learned

Lessons Learned will be updated shortly. More content is coming.

* Most of my lessons learned are in my code, here:

![CircuitPython_LCD_Code](/CircuitPython_LCD/Luke-Engineering_III-CircuitPython_LCD.py)

* Here is my hand-drawn circuit diagram:

![CicuitPython_LCD_Circuit_Diagram](/CircuitPython_LCD/Luke-Engineering_III-CircuitPython_LCD_Circuit_Diagram.pdf)

