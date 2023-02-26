#!/usr/bin/python

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

sense.set_rotation(0)

try:
	while True:
		sense.load_image("space_invader.png")
		sleep(1)
		sense.clear()
except KeyboardInterrupt:
	# Clear the sense hat when the display is over.
	sense.clear()
