from gpiozero import PWMLED
from signal import pause
from time import sleep

leds = [PWMLED(17), PWMLED(22), PWMLED(27)]

def start_traffic_lights():
	while True:
		leds[0].value = 1
		sleep(1)
		leds[0].value = 0
		leds[2].value = 1
		sleep(3)
		leds[2].value = 0
		leds[1].value = 1
		sleep(1)
		leds[1].value = 0

if __name__ == "__main__":
	start_traffic_lights()
