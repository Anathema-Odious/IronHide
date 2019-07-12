from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT, initial=GPIO.LOW)

n = 1
try:
	while True:
	    for x in range(1,n):
	        GPIO.output(8,GPIO.HIGH)
	        sleep(0.25) 
		GPIO.output(8,GPIO.LOW)
		sleep(0.25)
	    n = n+1
    	sleep (1)
except KeyboardInterrupt:
	print("Neeraj Interrupted.....")
