import random   #�פJ�üƼҲ�  #import standard library random

def  a():    #�إߤ@�ӷs��ƦW��a()
    return random.choice(['1','2','3','4','5','6'])
    
word = [a(),a(),a(),a()]    #�H���o��|�ӼƦr���᭱���j��

while True:   #�@�ӵL���j��
    for n in range(4) 
        for digit in digits:  #���Ҧ��O�ܦ��t��
            GPIO.output(digit, 1)   
        GPIO.output(digits[n], 0)    #�G��mn���O�աA�]���{�b�u��range(4)�ҥH����%4
        i = 0
        for on_or_off  in dictionary[word[n]]:   #���ަr���mn���r�A��for�j��G�ӫG���O��
            GPIO.output[segments[i],on_or_off)
            i += 1
        time.sleep(0.001)    #�C�ӤC�q��ܾ��G0.001��
    if GPIO.input(2) == True   #���s�}�����P��
        word = [a(),a(),a(),a()]   #�p�G�W����if�OTrue�N�|��@�ӷs���r��