# CicruitPython Servo 

For the CircuitPython Servo assignment, the goal was to wire up a servo to react to capacitive touch. In order to accomplish this, I had to download the latest version of CircuitPython from an external site, retrieve a CircuitPython servo file from a .lib folder from GitHub, and most importantly, problem solve.
The assignment was particularly difficult because little instruction was given. I had the help of my father and Dr. Shields to figure out the assignment, though I could have spent more time thinking about how to solve the problems that faced me.

Another takeaway from the assignment was the use of circuit diagrams. Fancy software is not needed in order to create a circuit diagram. A circuit diagram can be done by hand and the different components can be represented with common symbols.

## Lessons Learned
* Remember to look at all of the information present. It is usually useful or can be used to accomplish the goal.
* The Metro Express is only able to update when it is put in bootloader mode. 
* To go into bootloader mode, double click the reset button on the Metro Express.
* Once this is accomplished, the CIRCUITPY removable USB should show up as METROBOOT. The .UF2 file can now be uploaded onto the 
* Now, the updates can begin! Drag the desired files into the METROBOOT removable USB to update it. 
* I added an updated bootloader file and CircuitPython version.
* A bootloader file is created to upload information. I updated the boot loader for my Metro Express. One could say that I updated the updater.
* I found the bootloader file on a link provided in the assignment. I only found it after my dad pointed out that I should read the enitre page. 
* The .UF2 file is used to update CircuitPython. Usually, on a removable USB, there should be a README.md stating the current version.
* I updated my Metro Express to version 5.3.1. The version 6.0.0 was unstable so I did not use it.
