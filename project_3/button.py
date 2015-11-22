import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.IN)

while True:
  print GPIO.input(2)
  time.sleep(0.1)
# break the infinite loop by ctrl-c

GPIO.cleanup()