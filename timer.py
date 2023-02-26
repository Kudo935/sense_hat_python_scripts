#!/usr/bin/python

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
r = (255, 0, 0)

sense.set_rotation(0)

try:
	for i in range(9, -1, -1):
		sense.show_letter( str(i), r)
		sleep(1)
	sleep(1)
	sense.show_message("finish", 0.05, r)
	sleep(1)
	sense.clear()
except KeyboardInterrupt:
	# Clear the sense hat when the display is over.
	sense.clear()
