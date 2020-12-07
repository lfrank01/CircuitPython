import board
from digitalio import DigitalInOut, Direction, Pull

my_led = DigitalInOut(board.D3)
my_led.direction = Direction.OUTPUT

my_led.value = False

