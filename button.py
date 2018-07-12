from gpiozero import PWMLED, Button
from signal import pause


red_led = PWMLED(17)
button = Button(2)

red_led.source = button.values

pause()
