import RPi.GPIO as GPIO
import time
import urllib2
import re
import multiprocessing

URL = 'https://www.facebook.com/YUCSA12'
RE = '&#x80b2;&#x6210;&#x9ad8;&#x4e2d;&#x73ed;&#x806f;&#x6703;. (.),(...)'
STRING = 'Y118'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

segments = [5, 9, 17, 13, 19, 11, 4, 6]
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)

digits = [26, 10, 27, 22]
for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)

dictionary = {
    ' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,0,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1),
    'Y':(0,1,1,1,0,1,1),
    'O':(1,1,0,0,0,1,1),
    'P':(1,1,0,0,1,1,1),
    'S':(1,0,1,0,0,1,1)}

def display(S, no_use):
    n = 0
    while True:
        for digit in digits:
            GPIO.output(digit, 1)
        GPIO.output(digits[n], 0)
        i = 0
        for on_or_off in dictionary[S[n]]:
            GPIO.output(segments[i], on_or_off)
            i += 1
        time.sleep(0.005)
        n += 1
        n %= 4

def likes(U, R):
    page_source = urllib2.urlopen(U).readlines()
    #print page_source
    for line in page_source:
        match = re.search(R, line)
        if match:
            return match.group(1) + match.group(2)
    return 'OOPS'

while True:    
    p = multiprocessing.Process(target=display, args=(STRING, ''))
    p.start()
    STRING = likes(URL, RE)
    print STRING
    p.terminate()

GPIO.cleanup()