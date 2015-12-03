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
import pyaudio
import wave
import sys

#GPIO setup
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7 #Pin used for motion detecting
GPIO.setup(PIR_PIN, GPIO.IN)

#Sound setup
CHUNK = 1024

wf = wave.open('scream.wav', 'rb')
p = pyaudio.PyAudio()

stream = p.open(format = p.get_format_from_width(wf.getsampwidth(),
		channels = wf.getnchannels(),
		rate = wf.getframerate(),
		output = True)

data = wf.readframes(CHUNK)

try:
        print "PIR Module Test (CTRL + C to exit)"
        time.sleep(2)
        print "Ready"

        while True: #Main loop for motion detection.
                if GPIO.input(PIR_PIN):
			while len(data) > 0:
				stream.write(data)
				data = wf.readframes(CHUNK)
                        print "Motion Detected!"
                        time.sleep(2)                
                time.sleep(1)
	stream.stop_stream()
	stream.close()
	p.terminate()

except KeyboardInterrupt:
	stream.stop_stream()
	stream.close()
	p.teminate()
        print "Quit"
        GPIO.cleanup()
