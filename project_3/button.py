import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.IN)

while True:
  if GPIO.input(2):
    print 'Oh no!!!!'
  else:
    print 'Thank you...'
  time.sleep(0.1)
# break the infinite loop by ctrl-c

GPIO.cleanup()