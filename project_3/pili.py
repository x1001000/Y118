import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins = [10,9,11,5,6,13,19,26]

for each in pins:
  GPIO.setup(each, GPIO.OUT)
  GPIO.output(each, False)

def all_off():
  for each in pins:
    GPIO.output(each, False)

for i in range(len(pins)):
  all_off()
  GPIO.output(pins[i], True)
  time.sleep(0.5)
  
GPIO.cleanup()