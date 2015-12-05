"""
    Program by Matan Uchen.

    This program is was originally written in Python 2.7.
    After almost no deliberation I decided to move it to Python 3

    Using the GPIO pins and a PIR sensor, this program will detect
    movement. After detecting movement, it will print "Motion Deteced!"
    to the command line as well as playing the "scream2.wav" file.

    Here goes nothing...

    PIR Wires:
        VCC = Red
        OUT = Brown
        GND = Black

    GPIO Setup:
        VCC to 5v
        OUT to GPIO4
        GND to GND // duh...
"""

import RPi.GPIO as GPIO
import time

from pygame import mixer

""" GPIO SETUP """
sensor = 4 #GPIO4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)
""" END GPIO """

previous_state = False
current_state = False

# Music Function
def play():
    mixer.init()
    mixer.music.load('siren.mp3') # Change to whatever sound you want.
    mixer.music.play()
    time.sleep(5) # 2 for scream || 11 for Bass || 5 for siren
    mixer.music.stop()

print("Ready to start. CTRL + C to exit.")
while True: # Main Loop
    time.sleep(0.1)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
        if current_state:
            new_state = "HIGH"
            print("GPIO pin %s is %s" % (sensor, new_state))
            play()
        else:
            new_state = "LOW"
            print("GPIO pin %s is %s" % (sensor, new_state))



