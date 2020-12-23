# This main.py was modified from the original main.py of the assignment. This main.py file has additional code for
# cycling through colors and for randomly selecting colors.

import time
import board
import random

from rgb_pwm import RGB_PWM

# The rgb_pwm library was made for this assignment. It uses pulse-width modulation to drive common-anode RGB LEDs

r1 = board.D1
g1 = board.D2
b1 = board.D4
r2 = board.D5
g2 = board.D7
b2 = board.D9

# Digital IO pins that work with PWM: 1, 2, 3, 4, 5, 7, 9, 11, 12, and 13.
# Not 0, 6, 8, and 10.

myRGB1 = RGB_PWM(r1, g1, b1)  # This creates a new RGB object, using pins 3, 4, and 5.
myRGB2 = RGB_PWM(r2, g2, b2)  # This create a second RGB object, using pins 8, 9, and 10.

print("Static colors.")

myRGB1.red()  # Glow red.
myRGB2.green()  # Glow green.
time.sleep(2)
myRGB1.blue()  # Glow blue.
myRGB2.cyan()  # Glow... you get it...
time.sleep(2)
myRGB1.magenta()  # Did you know magenta isn't in the rainbow?
myRGB2.yellow()  # Like you learned in first grade, red and green make... huh?
time.sleep(2)

# Extra spicy (optional) part below.

#  Before rainbow tricks, turn off both LEDs.

myRGB1.dark()
myRGB2.dark()

time.sleep(1)
# Keep both LEDs off for 1 second.

rate1 = 2.0
rate2 = 3.0
# These variables are cycle rate in colors per second.

print("Here comes the rainbow.")

for rainbow_number in ["First", "Second", "Third"]:
    # The "rainbow_number" variable is created so that it can take on the values of "first," "second," and "third."
    # Instead of use the range function, by creating a list of strings, those strings can be factored into a print
    # statement.

    print(rainbow_number + " cycle.")
    # Note that a space is entered in " cycle" so that the serial monitor will separate the two strings.
    myRGB1.rainbow(rate1)
    myRGB2.rainbow(rate2)
    # Fade through the colors of the rainbow at the given rate. Oooooh, pretty!
    time.sleep(0.1)  # 100 cycles of 0.1 sec will take about 10 sec

print("Cycling through colors in nested loops.")

# What the code below does is have, for each instance of r_val, many instances of g_val. Then, for each increment
# of g_val, there are many instances of b_val. Because the g_val and b_val vary according to the r_val, the r_val is the
# most prominent color.

for r_val in range(0, 65535, 2048):
    # The arguments for "range" are (start, stop, stepsize). Stepsize will automatically be set to 1 unless told
    # otherwise.
    # Note that a stepsize of 2048 will result in 32 instances.
    for g_val in range(0, 65535, 2048):
        for b_val in range(0, 65535, 2048):
            myRGB1.custom_color(r_val, g_val, b_val)
            myRGB2.custom_color(65535 - r_val, 65535 - g_val, 65535 - b_val)

# The code below uses the "randrange" function from the "random" library.
# It makes one common-anode RGB LED a random color. At the same time, it makes the second common-anode RGB LED that
# colors "negative." A color "negative" is its opposite color.

print("Random colors until stopped.")

while True:
    b_val = random.randrange(0, 65535, 4096)
    r_val = random.randrange(0, 65535, 4096)
    g_val = random.randrange(0, 65535, 4096)

    # The RGB values are each randomly set to a PWM duty cycle at the start of the loop.

    # In the "custom_color" function, the r_val, g_val, and b_val are each set to a PWM duty cycle.
    myRGB1.custom_color(r_val, g_val, b_val)
    # One common-anode RGB LED is set to the "positive" color.
    myRGB2.custom_color(65535 - r_val, 65535 - g_val, 65535 - b_val)
    # The other common-anode RGB LED is set to the "negative" color.
    time.sleep(0.75)
