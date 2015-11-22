#!/usr/bin/python
#--------------------------------------   
# This script reads data from a 
# MCP3008 ADC device using the SPI bus.
#
# Analogue joystick version!
#
# Author : Matt Hawkins
# Date   : 17/04/2014
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------
import RPi.GPIO as GPIO
import time
import spidev
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins = [25,24,23,18,15,14]
i=0

for each in pins:
  GPIO.setup(each, GPIO.OUT)
  GPIO.output(each, False)

def all_off():
  for each in pins:
    GPIO.output(each, False)

def isLeft():
  return True if vrx_pos < 200 else False

def isRight():
  return True if vrx_pos > 800 else False

def move(i):
  all_off()
  GPIO.output(pins[i%6], True)


# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
    adc = spi.xfer2([1, (8+channel)<<4, 0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data
 
# Define sensor channels
# (channels 3 to 7 unused)
swt_channel = 0
vrx_channel = 1
vry_channel = 2

# Define delay between readings (s)
delay = 0.1

while True:

    # Read the joystick position data
    vrx_pos = ReadChannel(vrx_channel)
    vry_pos = ReadChannel(vry_channel)

    # Read switch state
    swt_val = ReadChannel(swt_channel)

    # Print out results
    print "--------------------------------------------"  
    #print("X : {}  Y : {}  Switch : {}".format(vrx_pos,vry_pos,swt_val))
    print("X : {}  Y : {}  ".format(vrx_pos,vry_pos))

    # Wait before repeating loop
    time.sleep(delay)

    if isLeft():
        i-=1
        move(i)
    if isRight():
        i+=1
        move(i)

  
GPIO.cleanup()