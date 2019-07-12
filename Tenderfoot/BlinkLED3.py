from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18,GPIO.OUT, initial=GPIO.LOW)

n = 1
try:
	while True:
	        GPIO.output(8,GPIO.HIGH)
		GPIO.output(18,GPIO.LOW)        	
		sleep(1) 
		GPIO.output(8,GPIO.LOW)
		GPIO.output(18,GPIO.HIGH)
        	sleep(1) 
			  
except KeyboardInterrupt:
	print("Neeraj Interrupted.....")
GPIO.cleanup()