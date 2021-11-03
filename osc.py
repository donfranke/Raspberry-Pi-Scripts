from gpiozero import LED
from time import sleep
from gpiozero import Button

button = Button(10)
led1= LED(17)
led2= LED(27)
led3= LED(22)
led4 = LED(9)
led5 = LED(11)
led6 = LED(5)
leds = [led1,led2,led3,led4,led5,led6]

timer = 0.1

def flash_lights():
    while(True):
        led1.on()
        sleep(timer)
        led1.off()
        led2.on()
        sleep(timer)
        led2.off()
        led3.on()
        sleep(timer)
        led3.off()
        led4.on()
        sleep(timer)
        led4.off()

def flash_lights_2():
    while(True):
        i = 0
        for led in leds:
            if(i>0):
                led.on()
                sleep(timer)
                led.off()
            i += 1

        i = 0
        for led in reversed(leds):
            if(i>0):
                led.on()
                sleep(timer)
                led.off()
            i += 1

flash_lights_2()