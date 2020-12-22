import time
import board
import random

from rgb_pwm import RGB_PWM

# The class and library that were made are imported.

r1 = board.D1
g1 = board.D2
b1 = board.D4
r2 = board.D5
g2 = board.D7
b2 = board.D9

# Digital IO pins that work with PWM: 1, 2, 3, 4, 5, 7, 9, 11, 12, and 13.
# Not 0, 6, 8, and 10.

print("Static colors")

myRGB1 = RGB_PWM(r1, g1, b1) # This creates a new RGB object, using pins 3, 4, and 5.
myRGB2 = RGB_PWM(r2, g2, b2)  # This create a second RGB object, using pins 8, 9, and 10.

myRGB1.red()  # Glow red.
myRGB2.green()  # Glow green.
time.sleep(2)
myRGB1.blue()  # Glow blue.
myRGB2.cyan()  # Glow... you get it...
time.sleep(2)
myRGB1.magenta()  # Did you know magenta isn't in the rainbow?
myRGB2.yellow()  # Like you learned in first grade, red and green make... huh?
time.sleep(2)

# Extra spicy (optional) part

#  Before rainbow tricks, turn off both LEDs.

myRGB1.dark()
myRGB2.dark()

time.sleep(1)

# Keep both LEDs off for 1 second.

# Cycle rate in colors per second

rate1 = 2.0
rate2 = 3.0

print("Here comes the rainbow!")

for rainbow_number in ["first", "second", "third"]:
    print(rainbow_number + " cycle")  # adding a string to a string makes a concatenated string
    myRGB1.rainbow(rate1)
    # Fade through the colors of the rainbow at the given rate. Oooooh, pretty!
    myRGB2.rainbow(rate2)
    # Fade through the colors of the rainbow at the given rate. Oooooh, pretty!
    time.sleep(0.1)  # 100 cycles of 0.1 sec will take about 10 sec

print("Cycling through colors in nested loops...")
# Cycle through colors
for r_val in range(0, 65535, 2048):  # range arguments are (start, stop, stepsize)
   for g_val in range(0, 65535, 2048):
       for b_val in range(0, 65535, 2048):
           myRGB1.custom_color(r_val, g_val, b_val)
           myRGB2.custom_color(65535-r_val, 65535-g_val, 65535-b_val)

print("Random colors until stopped...")
# Generate a random color and its "negative" and display on each LED
while True:
    b_val = random.randrange(0, 65535, 4096)
    r_val = random.randrange(0, 65535, 4096)
    g_val = random.randrange(0, 65535, 4096)
    myRGB1.custom_color(r_val, g_val, b_val)  # positive color
    myRGB2.custom_color(65535-r_val, 65535-g_val, 65535-b_val)  # its negative
    time.sleep(0.3)


