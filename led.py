from gpiozero import PWMLED
from signal import pause
from time import sleep

red_led = PWMLED(17)

amber_led = PWMLED(22)

green_led = PWMLED(27)

while True:
	red_led.value = 1
	sleep(1)
	red_led.value = 0
	green_led.value = 1
	sleep(3)
	green_led.value = 0
	amber_led.value = 1
	sleep(1)
	amber_led.value = 0

