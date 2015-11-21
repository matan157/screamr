# Screamer
# Created to fuck with mom.
# Using a PIR motion sensor, the pi will yell whenever someone walks by.

# Cables:
#	PIR-VCC: Red
#	PIR-OUT: Brown
#	PIR-GND: Black 

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 7 #Pin used for motion detecting

MOTION = False

GPIO.setup(PIR_PIN, GPIO.IN)

try:
        print "PIR Module Test (CTRL + C to exit)"
        time.sleep(2)
        print "Ready"

        while True: #Main loop for motion detection.
                if GPIO.input(PIR_PIN):
                        print "Motion Detected!"
                        time.sleep(2)                
                time.sleep(1)
except KeyboardInterrupt:
        print "Quit"
        GPIO.cleanup()
