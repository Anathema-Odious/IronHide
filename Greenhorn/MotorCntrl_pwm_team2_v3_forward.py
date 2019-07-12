import sys
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.cleanup()
time.sleep(1)
#Left Motor
Forward1=16
Backward1=18
Enable1=22
#Right Motor
Forward2=35
Backward2=33
Enable2=37
offset=0
Dia = 6.5
pi = 3.14
Circumference = pi*Dia
k_left=2.04573
k_right=2.416
R_left = 4.61
R_right =5.5
k_adjustment=1.1
k_adjustment_left=0.95
#rps=3
k_d=100/145.5
d=150*k_d
# max speed is 25 cm per second so t=d/25
t=4
v=d/t
rps=v/Circumference
V_left= k_left*rps*k_adjustment_left
V_right=k_right*rps*k_adjustment
dc_left= V_left*100/3.5
dc_right= V_right*100/3.5
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


    
def forward_pwm(x):
    f1=GPIO.PWM(Forward1,1000)
    f2=GPIO.PWM(Forward2,1000)
    f1.start(dc_left)
    f2.start(dc_right)
    #GPIO.output(Forward1,GPIO.HIGH) 
    #GPIO.output(Forward2,GPIO.HIGH)
    print("Moving Forward")
    time.sleep(x)
    GPIO.output(Backward1,GPIO.LOW)
    GPIO.output(Backward2,GPIO.LOW)
    f1.stop()
    f2.stop()



forward_pwm(t)
#t = Circumference*d
GPIO.output(Enable1,GPIO.LOW)
GPIO.output(Enable2,GPIO.LOW)
GPIO.cleanup()
