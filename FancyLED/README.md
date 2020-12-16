# Overview

The FancyLED assignment was somewhat of a continuation of the Classes, Objects, and Modules assignment. 
A `main.py` file was given, and the task was to create a library that suited the code. The main takeaway from this 
assignment was how to use lists. Lists are a handy way to group information and randomly select the information, as was 
done in the sparkle method.

In the `main.py` file, the methods required were alternate(), blink(), chase(), and sparkle(). Additionally, another 
method was created called all_off(). The method all_off() turned off the LEDs of an object. It was created for 
convenience. 

Note that the `digitalio` library was used for the assignment. I am still trying to understand the `pulseio` library.

# Circuit Diagram

The original circuit diagram of the assignment was as follows:

![FancyLED Origonal Circuit Diagram](/FancyLED/Luke-Engineering_III-FancyLED_Origonal_Circuit_Diagram.png)

However, the method by which the LEDs were wired was inefficient. Since I did not have enough wires to follow the
wiring diagram specifically, I used a wiring diagram that uses fewer wires but is as effective. 

Here is the revised wiring diagram: 

![FancyLED Revised Circuit Diagram](/FancyLED/Luke-Engineering_III-FancyLED_Revised_Circuit_Diagram.png)
#### Note - The revised circuit diagram was made on Tinkercad, which does not have an Adafruit Metro MO Express import option. The circuit diagram might be changed another time if a better circuit diagram creator if found.

# Lessons Learned 

* Specific items in a list do not need a self statement. Rather, the list had a self statement and can individually
  address the items in the list with code that would be like `self.list[number]`.
  
* To address multiple items at a time in a list, the code would be like `self.list[number1, number2, etc.`.

* When writing code that says `self.list[number]`, the [] serve to index the list. It is strange, but the indexing
  begins at 0. For example, `self.led_list[0]` would refer to the first item in the list.
  
* The `range` method can be used to loop code a specified number of times. Range can be set between 0 and a variable.
  It is helpful because, in a method, the variable can be set a standard but then also changed. The `range` method allows
  The code in the `main.py` to specify the number of loops that is wanted for a method.
  
* Using `%2` in `if alternate_number % 2 == 0:` divides the `alternate_number` by 2 and then looks at the remainder.
  It is useful with the `range` function because if the range increases by whole numbers, it will either be an even number
  (remainder = 0), or an odd number (remainder does not = 0). Two opposite options were created using this idea, as 
  can be seen in the alternate method.

* My code comments explain most of how the code works. Here is my library code:
  [fancyLED.py](/FancyLED/fancyLED.py)
  
* Below is the `main.py` file that imported the `rgb.py` library:
  [main.py](/FancyLED/main.py)
  
* Additionally, my father recommended that I should not change the name of my `main.py` files because it creates 
  unnecessary confusion.
  
# On Using Black As A Code Reformatter

The tool "black" is a code reformatter that can work with any python (.py) file. Black reformats code into a standard 
format, making orgnaization simple and consistnet.

To use back, open a terminal window in the same directory as the file and for example: black fancyLED.py

Here it the link to black:
[Link to black](https://pypi.org/project/black/)

