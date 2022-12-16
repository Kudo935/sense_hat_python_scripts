#!/usr/bin/python
from sense_hat import SenseHat

sense = SenseHat()

sense.set_rotation(90)

try:
	while True:
		t = sense.get_temperature()
		p = sense.get_pressure()
		h = sense.get_humidity()
		t = round(t, 1)
		p = round(p, 1)
		h = round(h, 1)
		msg = "Temp = %s Pressure = %s Humidity = %s" % (t, p, h)
		sense.show_message(msg, scroll_speed=0.07)
except KeyboardInterrupt:
	# Clear the sense hat when the display is over.
	sense.clear()
