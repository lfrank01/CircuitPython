# Hello CircuitPython
## Overview

The Hello CircuitPython assignment explained how to set up CircuitPython with my Metro Express. At the end of it, I was able to run my first code!

The proccess of setting up CircuitPython varies for different devices:

* For a Cromebook, use Caret for code and Beagle Term for a serial monitor.
* For a Mac or PC, use Mu. Mu incorporates code editing and a serial monitor.
* Keep in mind that for CircuitPython code editing, any text editor can be used. The file that the code is edited on will likely need a .py at the end of it to signify that it is CircuitPython.

For this assignment, I did my work on Chromebook. After downloading Caret and Beagle Term on the Google Play Store for Chromebook, here is how I proceeded:

* Plug in the Metro Express. It should apear as a removable file. 
* In Caret, select the upload file option and find the Metro Express
* The screen should look like this:

![Metro Express Pop-Up](/Hello_CircuitPython/Luke-Engineering_III-Metro_Express_Pop_Up.png)

* Click on the main.py file. A .py file pertains to CircuitPython.
* The file should have lots of text. If it is run, the Metro Express should perform something with the built in LED.
* Now that the text editor knows that it is editing CircuitPython, the large amount of code can be deleted. When typing new code, there should be color effects.
* Here is what my code looked like: 

![Hello_CircuitPython Code Screenshot](/Hello_CircuitPython/Luke-Engineering_III-Hello_CircuitPython_Screenshot.png)

* Note that C++ uses "void loop()" with { } to run the main code. CircuitPython uses  "while True:" 
* It is helpful to note that a piece of code in CircuitPthon that performs a function will have () after it. To create color using RGB (Red Green Blue), the code is dot.fill((0,100,0)). There are two parethesis because the function is including a variable. The numbers each corespond to primary colors. The order of them is red, green, and blue.
* I could have listed a variable earlier in the code. It would say something like red = (100,0,0) and then later on in my code I would write dot.fill(red).
* Note that variables in CircuitPython do not have a semicolon (;) at the end.
* Finally, it is helful to have a serial monitor when writing code. For Chromebook, I used Beagle Term.
* After opening up Beagle Term and connecting it to the Metro Express, the print("") function will write text into it. This is helpful for debugging. 

Here is the link to my code, which is listed as a seperate file in this folder. Note that a hashtag (#) means that the code is a comment and will not run. Another tip is that saving a file as a .py file will often add CircuitPython effects. At least, for Atom.io.

![Hello_CircuitPython Code](/Hello_CircuitPython/Luke-Engineering_III-Hello_CircuitPython.py)
