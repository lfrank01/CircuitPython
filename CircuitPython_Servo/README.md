# CicruitPython Servo 

#### Note - I worked on PC for the assignment. Since I had not installed the CircuitPython packages on Atom.io, I used Mu. Mu is a decent piece of software that has a debugging setting, but the built-in serial monitor was acting funky and there is no "save as" feature. I want to switch to Atom.io or PyCharm.

## Overview
For the CircuitPython Servo assignment, the goal was to wire up a servo to react to capacitive touch. In order to accomplish this, I had to download the latest version of CircuitPython from an external site, learn how to be a better Google-er, and most importantly, problem solve.

The assignment was particularly difficult because little instruction was given. I had the help of my father and Dr. Shields to figure out the assignment. Though, I could have spent more time thinking about how to solve the problems that I faced.

Another takeaway from the assignment was the use of circuit diagrams. Fancy software is not needed in order to create a circuit diagram. A circuit diagram can be done by hand and the different components can be represented with common symbols.

#### Note - It is important to understand what duty cycle and PMW are in servo control. I was confused about it and had my dad explain it. PMW is the frequency of the wavelength that the servo reads, meaning how many times in one standardized time it will go up and down. Duty cycle is when that wavelength is read as on and off.

![Duty Cycle Picture](/CircuitPython_Servo/Luke-Engineering_III-Duty_Cycyle.py)

## Lessons Learned
* Remember to look at all of the information present. If it has been assigned, it is usually useful to accomplish the task at hand.
* The Metro Express is only able to update when it is put in bootloader mode. 
* To go into bootloader mode, double click the reset button on the Metro Express.
* Once this is accomplished, the CIRCUITPY removable USB should show up as METROBOOT. The .UF2 file can now be uploaded:
* Now, the updates can begin! Drag the desired files into the METROBOOT removable USB to update it. 
* I added an updated bootloader file and CircuitPython version.
* A bootloader file is created to upload information. I updated the boot loader for my Metro Express. One could say that I updated the updater.
* I found the bootloader file on a link provided in the assignment. I only found it after my dad pointed out that I should read the enitre page. 
* The .UF2 file is used to update CircuitPython. Usually, on a removable USB, there should be a README.md stating the current version.
* I updated my Metro Express to version 5.3.1. The version 6.0.0 was unstable so I did not use it.

* I rigged up my code to get the micro serve, not continuous servo, to move forward when I touched a wire, and backward when I touched another. I added debugging, which is super important, by including LED and serial monitor code. 
* I also added code to make it so that when neither wire was pressed, the LED would turn off and a message would show up. Additionaly, I made it so that when I pressed both wires at the same time, the servo angle reset to 90 and the light turned purple.

* Most of my lessons learned are in my code, here:

![CircuitPython Servo Code](/CircuitPython_Servo/Luke-Engineering_III-CircuitPython_Servo.py)

* Here is my hand-drawn circuit diagram:

![CicuitPython Servo Circuit Diagram](/CircuitPython_Servo/Luke-Engineering_III-CicuitPython_Servo_Circuit_Diagram)

