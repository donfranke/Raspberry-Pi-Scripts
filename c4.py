from gpiozero import LED
from time import sleep

led1= LED(17)
led2= LED(27)
led3= LED(22)
timer = 0.1

while True:
    led1.on()
    sleep(timer)
    led1.off()
    led2.on()
    sleep(timer)
    led2.off()
    led3.on()
    sleep(timer)
    led3.off()
