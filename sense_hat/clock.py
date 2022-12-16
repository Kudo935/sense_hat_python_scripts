#!/usr/bin/env python

from sense_hat import SenseHat
from time import sleep, strftime
from random import randint
import threading

sense = SenseHat()
today = strftime("%d")
month = strftime("%B")
year = strftime("%Y")
Green = (0, 255, 0)

sense.set_rotation(0)

try:
    while True:
        sense.show_message(
        today,
        text_colour=Green,
        scroll_speed=0.08,
        )
        sense.clear()
        sense.show_message(
        month,
        text_colour=Green,
        scroll_speed=0.08,
        )
        sense.clear()
        sense.show_message(
        year,
        text_colour=Green,
        scroll_speed=0.08,
        )
        sense.clear()
except KeyboardInterrupt:
	# Clear the sense hat when the display is over.
	sense.clear()
