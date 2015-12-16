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