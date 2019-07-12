from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
led_list = (8,18)
GPIO.setup(led_list,GPIO.OUT, initial=GPIO.LOW)

try:
	while True:
	        GPIO.output(led_list,(True,False))        	
		sleep(1) 
		GPIO.output(led_list,(False,True))
        	sleep(1) 
			  
except KeyboardInterrupt:
	print("Neeraj Interrupted.....")
GPIO.cleanup()