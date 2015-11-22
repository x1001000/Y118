R_last = 0
LED_state = 0
while True:
  R_now = input("R(ohm) value of the resistor: ")
  if R_now >= 0.8 and R_last < 0.8:
    LED_state += 1
  R_last = R_now
  print 'Light ON' if LED_state%2 else 'light OFF'