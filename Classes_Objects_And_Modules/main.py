import time
import board

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

print("Test.")

myRGB1 = RGB_PWM(r1, g1, b1)  # This creates a new RGB object, using pins 3, 4, and 5.
myRGB2 = RGB_PWM(r2, g2, b2)  # This create a second RGB object, using pins 8, 9, and 10.

myRGB1.red()  # Glow red.
myRGB2.green()  # Glow green.
time.sleep(5)
myRGB1.blue()  # Glow blue.
myRGB2.cyan()  # Glow... you get it...
time.sleep(5)
myRGB1.magenta()  # Did you know magenta isn't in the rainbow?
myRGB2.yellow()  # Like you learned in first grade, red and green make... huh?
time.sleep(5)

# Extra spicy (optional) part

#  Before rainbow tricks, turn off both LEDs.

myRGB1.dark()
myRGB2.dark()

time.sleep(1)

# Keep both LEDs off for 1 second.

# Cycle rate in colors per second

rate1 = 2.0
rate2 = 3.0

while True:
    myRGB1.rainbow(rate1)
    # Fade through the colors of the rainbow at the given rate. Oooooh, pretty!
    myRGB2.rainbow(rate2)
    # Fade through the colors of the rainbow at the given rate. Oooooh, pretty!
    time.sleep(0.1)
