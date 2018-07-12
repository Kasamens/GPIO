from gpiozero import PWMLED
from time import sleep

leds = [PWMLED(17), PWMLED(22), PWMLED(27), PWMLED(23), PWMLED(24)]

while True:
	
	for led in leds:
		led.value = 1
		sleep(.1)
		led.value = 0
