'''
import random   #匯入亂數模組  #import standard library random

def  a():    #建立一個新函數名為a()
    return random.choice(['1','2','3','4','5','6'])
    
word = [a(),a(),a(),a()]    #隨機得到四個數字做後面的迴圈

while True:   #一個無限迴圈
    for n in range(4) 
        for digit in digits:  #讓所有燈變成暗的
            GPIO.output(digit, 1)   
        GPIO.output(digits[n], 0)    #亮位置n的燈組，因為現在只有range(4)所以不用%4
        i = 0
        for on_or_off  in dictionary[word[n]]:   #索引字典位置n的字，用for迴圈亮該亮的燈管
            GPIO.output[segments[i],on_or_off)
            i += 1
        time.sleep(0.001)    #每個七段顯示器亮0.001秒
    if GPIO.input(2) == True   #按鈕開關的感測
        word = [a(),a(),a(),a()]   #如果上面的if是True就會找一個新的字串
'''

import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.IN)

segments = (5, 9, 17, 13, 19, 11, 4, 6)
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)

digits = (26, 10, 27, 22)
for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)

dictionary = {' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),}

def a():
    return random.choice(['1','2','3','4','5','6'])

word=[a(),a(),a(),a()]

while True:
  for n in range(4):
      for digit in digits: # all digits off
          GPIO.output(digit, 1)
      GPIO.output(digits[n], 0)
      i = 0
      for on_or_off in dictionary[word[n]]:
          GPIO.output(segments[i], on_or_off)
          i += 1
      time.sleep(0.001)
  if GPIO.input(2) == True:
      word=[a(),a(),a(),a()]

GPIO.cleanup()
