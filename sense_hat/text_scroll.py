#!/usr/bin/python

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

Text = "SenseHat ist awesome!"
Letter = "X"

Blue = (0, 0, 255)
Green = (0, 255, 0)
White = (255, 255, 255)
Black = (0, 0, 0)

sense.set_rotation(0)

try:
	while True:
		sense.show_message(
			Text, 
			text_colour=White, 
			back_colour=Black, 
			scroll_speed=0.02		# 0.1 is normal
		)
		sleep(2)
		sense.show_letter(
			Letter,
			text_colour=White, 
			back_colour=Black
		)
		sleep(2)
		sense.clear()
		sleep(2)
except KeyboardInterrupt:
	# Clear the sense hat when the display is over.
	sense.clear()
