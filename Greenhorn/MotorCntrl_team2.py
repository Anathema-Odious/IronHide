import sys
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.cleanup()
Forward=16
Backward=18
Enable=22
sleeptime=1
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Forward,GPIO.OUT)
GPIO.setup(Backward,GPIO.OUT)
GPIO.setup(Enable,GPIO.OUT)

def forward(x):
    GPIO.output(Enable,GPIO.HIGH)
    GPIO.output(Forward,GPIO.HIGH)
    print("Moving Forward")
    time.sleep(x)
    GPIO.output(Forward,GPIO.LOW)

def reverse(x):
    GPIO.output(Enable,GPIO.HIGH)
    GPIO.output(Backward,GPIO.HIGH)
    print("Moving Backward")
    time.sleep(x)
    GPIO.output(Backward,GPIO.LOW)

def forward_pwm(x,dc):
    GPIO.output(Enable,GPIO.HIGH)
    p=GPIO.PWM(Forward,1000)
    p.start(dc)
    time.sleep(x)
    p.stop()
   

def reverse_pwm(x,dc):
    GPIO.output(Enable,GPIO.HIGH)
    p=GPIO.PWM(Backward,1000)
    p.start(dc)
    time.sleep(x)
    p.stop()

#while(1):
    #for dc in range(0,100,10):
    
        #forward_pwm(1,dc)

        #reverse_pwm(1,dc)
forward(1)

#reverse(1)
time.sleep(2)
GPIO.output(Enable,GPIO.LOW)
   

GPIO.cleanup()
