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

![Origonal FancyLED Circuit Diagram]()


# Lessons Learned 

* Specific items in a list do not need a self statement. Rather, the list had a self statement and can individually
  address the items in the list with code that would be like `self.list[number]`.
  
* To address multiple items at a time in a list, the code would be like `self.list[number1, number2, etc.`.

* When writing code that says `self.list[number]`, the [] serve to index the list. It is strange, but the indexing
  begins at 0. For example, self.led_list[0] would refer to the first item in the list.
  
* The `range` method can be used to loop code a specified number of times. Range can be set between 0 and a variable.
  It is helpful because, in a method, the variable can be set a standard but then also changed. The `range` method allows
  The code in the `main.py` to specify the number of loops that is wanted for a method.
  
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

