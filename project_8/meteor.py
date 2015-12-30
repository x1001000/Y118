import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

row = [2,3,4,17,27,14,15,18]
col = [26,19,13,6,5,11,9,10]

for r in row:
    GPIO.setup(r, GPIO.OUT)
    GPIO.output(r, 0)

for c in col:
    GPIO.setup(c, GPIO.OUT)
    GPIO.output(c, 1)
    time.sleep(1)
