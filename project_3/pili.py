import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins = [14,15,18,23,24,25,8,7]

for each in pins:
  GPIO.setup(each, GPIO.OUT)
  GPIO.output(each, False)

def all_off():
  for each in pins:
    GPIO.output(each, False)
    
while True:
  for i in range(len(pins)):
    all_off()
    GPIO.output(pins[i], True)
    time.sleep(0.1)
  
GPIO.cleanup()