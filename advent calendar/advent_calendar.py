#!/usr/bin/python

from sense_hat import SenseHat
from time import sleep, strftime

sense = SenseHat()
sense.set_rotation(0)

# Colours
colours = {
    'r' : [255, 0, 0],
    'o' : [255, 125, 0],
    'y' : [255, 255, 0],
    'g' : [0, 255, 0],
    'b' : [0, 0, 255],
    'i' : [75, 0, 130],
    'v' : [159, 0, 255],
    'n' : [135, 80, 22],
    'w' : [255, 255, 255],
    'e' : [0, 0, 0]  # e stands for empty/black
    }
# Pictures
f = open("pictures.txt", "r")
all_pics = f.readlines()
door = all_pics[0]

# Display a given picture string on the sense HAT
def display_pic(pic_string):
  
  pic_string = pic_string.strip("\n")
  pic_string = pic_string.split(",")

  pic_list = []
  for letter in pic_string:
      pic_list.append(colours[letter])
  
  sense.set_pixels(pic_list)

try:
  while True:
    # Clear the page and display a question mark
    sense.clear()
    display_pic(door)
    # Wait for the joystick to be pressed to open the door
    event = sense.stick.wait_for_event()

    if event.action == "pressed" and event.direction == "middle":
      # Show which day it is
      today = strftime("%d")
      month = strftime("%B")
    
      if today == "25" and month == "December":
        sense.show_message("Happy Christmas!")
      elif int(today) > 25 or month != "December":
        sense.show_message("Keep waiting!")
      else:
        sense.show_message( today )
        # Get the picture for today as a string and display it
        picture = all_pics[int(today)]
        display_pic(picture)
        sleep(10)
except KeyboardInterrupt:
  # Clear the sense hat when the display is over.
  sense.clear()
