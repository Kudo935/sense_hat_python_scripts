#!/usr/bin/python

from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

try:
	while True:
		x = randint(0, 7)
		y = randint(0, 7)
		z = randint(0, 7)
		a = randint(0, 7)
		r = randint(0, 255)
		g = randint(0, 255)
		b = randint(0, 255)
		sense.set_pixel(x, y, r, g, b)
		sleep(0.01)
		sense.set_pixel(z, a, 0, 0, 0)
		sleep(0.01)
except KeyboardInterrupt:
	# Clear the sense hat when the display is over.
	sense.clear()
