# Screamer
# Created to fuck with mom.
# Using a PIR motion sensor, the pi will yell whenever someone walks by.

# Cables:
#	PIR-VCC: Red
#	PIR-OUT: Brown
#	PIR-GND: Black

#Pi GPIO Config:
#       Red: Pin 2
#       Black: Pin 6
#       Brown: Pin 26

#Breadboard
#       PIR-VCC + Red: Positive Rail
#       PIR-GRD + Black: Negative Rail
#       PIR-OUT + Brown: Same Rail (Used 3B + 3C)

import RPi.GPIO as GPIO
import time

from Tkinter import *
root - Tk()

import tkSnack
tkSnack.initializeSnack(root)

#GPIO setup
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7 #Pin used for motion detecting
GPIO.setup(PIR_PIN, GPIO.IN)

#Sound setup
sound = tkSnack.Sound(load='./scream.wav')

try:
        print "PIR Module Test (CTRL + C to exit)"
        time.sleep(2)
        print "Ready"

        while True: #Main loop for motion detection.
                if GPIO.input(PIR_PIN):
                        sound.play()
                        print "Motion Detected!"
                        time.sleep(2)                
                time.sleep(1)
except KeyboardInterrupt:
        print "Quit"
        GPIO.cleanup()
