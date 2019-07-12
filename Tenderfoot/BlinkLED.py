import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT, initial=GPIO.LOW)
while True:
    GPIO.output(8,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(8,GPIO.LOW)
    time.sleep(0.5)