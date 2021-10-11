import time
import board
import digitalio

print("hello blinky!")

led1= digitalio.DigitalInOut(board.D18)
led2= digitalio.DigitalInOut(board.D17)
led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT

while True:
    led1.value = True
    time.sleep(0.1)
    led1.value = False
    time.sleep(0.1)
    led2.value = True
    time.sleep(0.1)
    led2.value = False
    time.sleep(0.1)
