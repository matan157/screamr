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

""" SOUND SETUP """
mixer.init()
mixer.music.load('./scream2.wav')
""" SOUND END """

previous_time = time.time() 
elapsed_time = 0

previous_state = False
current_state = False

while True: # Main Loop
    time.sleep(0.1)
    previous_state = current_state
    elapsed_time = time.time() - previous_time 
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
        if current_state:
            new_state = "HIGH"
            if elapsed_time <= 5:
                mixer.music.play()
                time.sleep(2)
                previous_time = time.time() 
        else:
            new_state = "LOW"
        print("GPIO pin %s is %s" % (sensor, new_state))
        mixer.music.stop()



