# CircuitPython_LCD

## Overview

For the CircuitPython LCD assignment, there were several subtle parts that made the creation of the code difficult. Luckily, I had the help of my father, who happens to be an engineer. The goal of the assignment was to wire up an LCD so that when one wire was pressed, a counter would move up by one, and when another wire was pressed, the counter would move down by one. Furthermore, the counter was supposed to only go up after each press, and not continue to go up when holding down a wire.

In order to accomplish this, there was a repository that contained LCD code suited for Metro Express and another repository that contained code to update the adafruit_bus_library. In the LCD repository, there was a file named "i2c_pcf8574_interface.py," which made the LCD backpack work. A key note was that the author of the file used a microcontroller library instead of time.sleep(), because it was more accurate; except, he forgot to include an import of the microcontroller library in his code, so the code did not work.

That file is updated in [my repository.](https://github.com/lfrank01/CircuitPython/blob/main/CircuitPython_LCD/i2c_pcf8574_interface.py)

The website [CircuitPython Read The Docs](https://readthedocs.org/projects/circuitpython/) was a helpful tool, as it allowed me to search for the libraries that were needed.

Another note was that the Metro MO Express may not have had the memory to run the i2c code, among other large libraries such as capacitive touch. As a solution, Dr. Shields converted the (.py) libraries into (.mpy) files, which are compressed. This was a smart decision. However, I did not do it, because an (.mpy) file is not human-readable, and I wanted to be able to understand the libraries.

## Lessons Learned

* A bus driver is used for the communication and transportation of data between seperate components. The (adafruit_bus_driver) was used for the communication between the Metro M0 Express and i2c LCD backpack. 

* An LCD without an LCD backback runs a parallel circuit, meaning that for the eight data wires (also known as "8-bit") all run at the same time and read as a 0 or 1. The combination of those zeros and ones is what the LCD reads and interprets.

* The i2c backpack changes the parallel interface of the LCD into a serial one. A serial interface recieves bits of data one at a time. To remember this, think of a TV series, where there are subsequent episodes. The advantages of a serial circuit is that fewer wires and pins are needed.

Here is what an LCD backpack looks like:

![CircuitPython_LCD_Screenshot](/CircuitPython_LCD/Luke-Engineering_III-CircuitPython_LCD_Backpack.png)

#### Note - Work Cited for the website that I screenshoted this image from:
Developer, Wired, et al. “Wiring I2C Module on 16×2 LCD with SCL/SDA.” 14core.Com, www.14core.com/wiring-i2c-module-on-16x2-lcd-with-sclsda/. 
#### I used EasyBib for generating a citation an MLA citation.

* Maybe you are wondering what an i2c device is. Well, an i2c device (Inter-Integrated Circuit), which is what the LCD backpack is, only has two bus wires: (SDA) and (SCL), along with a ground and power source.

* The (SDA) wire stands for (Serial Data Wire) and transmits the data one bit at a time.

* The (SCL) wire stands for (Serial Clock Wire) and tells the (SDA) wire when to read the 8-bit data.

* Note that the (SDA) and (SCL) wires have pins with coresponding names on the Adafruit Metro MO Express.

* A (.py) file is standard CircuitPython code. A (.mpy) is a micropython file, which compresses CircuitPython code into a compressed format. A (.mpy) file is helpful for data storage, but because it converts the code into an unreadable and unreversable format, it makes it hard to understand the libraries.

* Some i2c LCD backpacks have an adress that needs to be found and used in the code. I explain how to do this in the code. There were two main addresses that were used: "0x27" and "0x3f." One of those addresses should work.

* My code comments explain most of how the code works. Here is a link to my code:
[CircuitPython_LCD_Code.](/CircuitPython_LCD/Luke-Engineering_III-CircuitPython_LCD.py)

* Also, here is my hand-drawn circuit diagram:
[CicuitPython_LCD_Circuit_Diagram.](/CircuitPython_LCD/Luke-Engineering_III-CircuitPython_LCD_Circuit_Diagram.pdf)

