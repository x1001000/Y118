import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pins = (2, 3, 4)

for each_led_pin in led_pins:
    GPIO.setup(each_led_pin, GPIO.OUT)
    GPIO.output(each_led_pin, False)

i=0
'''
while True:
  for each_led_pin in led_pins:
      GPIO.output(each_led_pin, False)
  GPIO.output(led_pins[i], True)
  i+=1
  i%=3
  time.sleep(1)
'''

while True:
  GPIO.output(led_pins[i], True)
  time.sleep(0.3)
  GPIO.output(led_pins[(i+1)%3], False)
  GPIO.output(led_pins[(i+2)%3], False)
  time.sleep(0.7)
  i+=1
  i%=3

GPIO.cleanup()