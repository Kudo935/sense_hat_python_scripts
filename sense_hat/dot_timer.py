#!/usr/bin/python

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 0)

s = 32

sense.set_rotation(0)

timer = []

try:
	for i in range(64):
		if i < s :
			timer.append(r)
		else:
			timer.append(b)
	sense.set_pixels(timer)

	for i in range(0, s):
		sleep(1)
		timer[i] = g
		sense.set_pixels(timer)

	for i in range(0, 10):
		sense.clear()
		sleep(0.1)
		sense.set_pixels(timer)
		sleep(0.1)
	sense.clear()
except KeyboardInterrupt:
	# Clear the sense hat when the display is over.
	sense.clear()

