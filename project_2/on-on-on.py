import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

push = 17
buzz = 4

GPIO.setup(push, GPIO.IN)
p = GPIO.PWM(buzz, 50)

freq = {    'C3':  131,
            'D3':  147,
            'E3':  165,
            'F3':  175,
            'G3':  196,
            'A3':  220,
            'B3':  247,
            'C4':  262,
            'D4':  294,
            'E4':  330,
            'F4':  349,
            'G4':  392,
            'A4':  440,
            'B4':  494,}

melody = [  'G3','C4','C4','E4','A4','E4','G4',
            'G4','A4','G4','E4','F4','E4','D4',
            'A3','D4','D4','F4','B4','B4','A4','G4',
            'F4','F4','F4','E4','A3','B3','C4','D4']

note = 0
while True:
    #while push == 0:
        #time.sleep(0.002)
    #while push == 1:
        p.ChangeFrequency(freq[melody[note]])
        time.sleep(1)
        note += 1
        note %= 30
