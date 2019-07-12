import sys
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.cleanup()
Forward1=16
Backward1=18
Enable1=22
Forward2=35
Backward2=33
Enable2=37
offset=15

sleeptime=1
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Forward1,GPIO.OUT)
GPIO.setup(Backward1,GPIO.OUT)
GPIO.setup(Enable1,GPIO.OUT)
GPIO.setup(Forward2,GPIO.OUT)
GPIO.setup(Backward2,GPIO.OUT)
GPIO.setup(Enable2,GPIO.OUT)
GPIO.output(Enable1,GPIO.HIGH)
GPIO.output(Enable2,GPIO.HIGH)

def forward(x):
   
    GPIO.output(Forward1,GPIO.HIGH) 
    GPIO.output(Forward2,GPIO.HIGH)
    print("Moving Forward")
    #time.sleep(x)
    GPIO.output(Backward1,GPIO.LOW)
    GPIO.output(Backward2,GPIO.LOW)

def reverse(x):
    GPIO.output(Backward1,GPIO.HIGH)
    GPIO.output(Backward2,GPIO.HIGH)
    print("Moving Backward Motor 1")
    #time.sleep(x)
    GPIO.output(Forward1,GPIO.LOW)
    GPIO.output(Forward2,GPIO.LOW)
    
def forward_pwm(x,dc):
    f1=GPIO.PWM(Forward1,1000)
    f2=GPIO.PWM(Forward2,1000)
    f1.start(dc)
    f2.start(dc+offset)
    #GPIO.output(Forward1,GPIO.HIGH) 
    #GPIO.output(Forward2,GPIO.HIGH)
    print("Moving Forward")
    time.sleep(x)
    GPIO.output(Backward1,GPIO.LOW)
    GPIO.output(Backward2,GPIO.LOW)
    f1.stop()
    f2.stop()

def reverse_pwm(x,dc):
    r1=GPIO.PWM(Backward1,1000)
    r2=GPIO.PWM(Backward2,1000)
    r1.start(dc);
    r2.start(dc);
    #GPIO.output(Backward1,GPIO.HIGH)
    #GPIO.output(Backward2,GPIO.HIGH)
    print("Moving Backward Motor 1")
    time.sleep(x)
    GPIO.output(Forward1,GPIO.LOW)
    GPIO.output(Forward2,GPIO.LOW)
    r1.stop()
    r2.stop()
    



#while(1):
    #for dc in range(0,100,10):
    
        #forward_pwm(1,dc)

        #reverse_pwm(1,dc)
#forward(0)
forward_pwm(10,50)
#time.sleep(10)
#reverse(0)
reverse_pwm(10,50)
#reverse2(0)

#time.sleep(10)

GPIO.output(Enable1,GPIO.LOW)
GPIO.output(Enable2,GPIO.LOW)


GPIO.cleanup()
