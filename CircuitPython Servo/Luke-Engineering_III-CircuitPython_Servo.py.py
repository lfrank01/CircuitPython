import time
import board
import pulseio
import neopixel
from adafruit_motor import servo
import touchio

pwm = pulseio.PWMOut(
                    # (polseio) is the directory.
                    # (.PMWOut) is a folder inside of that directory.
                    # The indented codes below are the
                    # Parameters of the (.PMWOut) folder.
                    pin=board.A2,
                    duty_cycle=2 ** 15,
                    # A (**) signifies "to the power of."
                    # A (*) signifies "all of."
                    # For example, from touchio import *.
                    frequency=50
                    # Stylizing code in this indented format
                    # makes it understandable.
                    )


dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

# Why must (board.NEOPIXEL.1) 1 be listed?
# Are there multiple built-in neopixels in the Metro Express?

my_servo = servo.Servo(pwm)

touch_A3 = touchio.TouchIn(board.A3)

touch_A4 = touchio.TouchIn(board.A4)

# Metro Express pins A0-A5 are compatible with capacitive touch.

# Metro Express pins A0, A1, and A5 are NOT compatible with a servo.

my_servo.angle = 90

while True:
    if touch_A3.value:
        print("A3 touched")
        dot.fill((0, 0, 100))
        my_servo.angle = min(
                            # The (min feature takes the values inside
                            # Parenthesis and chooses the smallest.
                            # It was used to set paremeters for
                            # The (my_servo.angle) value.
                            my_servo.angle + 1,
                            180
                            )

        time.sleep(0.01)

    if touch_A4.value:
        print("A4 touched")
        dot.fill((100, 0, 0))
        # (Serial.print) and (dot.fill) are proficient debuggers.
        my_servo.angle = max(
                            # The (max feature takes the values
                            # inside parenthesis and chooses the largest.
                            # It was used to set paremeters for
                            # The (my_servo.angle) value.
                            my_servo.angle - 1,
                            0
                            )
        time.sleep(0.01)

    if touch_A3.value and touch_A4.value:
        print("A3 and A4 touched. Reset to 90 degrees.")
        my_servo.angle = 90
        dot.fill((1, 1, 1))  #
        # (dot.fill((1,1,1))) causes the color to be purple.

    else:
        # The (if)function is triggered by an action.
        # The (else) function is triggered by the absence of that action.
        print("Nothing touched")
        dot.fill((0, 0, 0))
