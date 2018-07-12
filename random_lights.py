import random
from gpiozero import PWMLED
from time import sleep

leds = [PWMLED(17), PWMLED(22), PWMLED(27), PWMLED(23), PWMLED(24)]

def start_random_lights():
	while True:
		num = random.randrange(0,len(leds))
		num2 = random.randrange(1,10)
		
		leds[num].value = 1
		sleep(num2/10)
		leds[num].value = 0

if __name__ == "__main__":
	start_random_lights()
