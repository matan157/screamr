from pygame import mixer
import time

mixer.init()
mixer.music.load('scream2.wav')
mixer.music.play(-1)
time.sleep(10)
mixer.music.stop()
