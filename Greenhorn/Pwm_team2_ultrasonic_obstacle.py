import sys
import RPi.GPIO as GPIO
import time
import array
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
#Configuration Motors
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Forward1,GPIO.OUT)
GPIO.setup(Backward1,GPIO.OUT)
GPIO.setup(Enable1,GPIO.OUT)
GPIO.setup(Forward2,GPIO.OUT)
GPIO.setup(Backward2,GPIO.OUT)
GPIO.setup(Enable2,GPIO.OUT)
GPIO.output(Enable1,GPIO.HIGH)
GPIO.output(Enable2,GPIO.HIGH)

#Ultrasonic Sensor
GPIO_TRIGGER=32
GPIO_ECHO=40
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
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
v_max=25
#rps=3
k_d=100/145.5

d=150*k_d
# Steering Related Parameters
dist_reverse=10
track=14
arc_right_angle=pi*track/2
# max speed is 25 cm per second so t=d/25
def duty_cycle(dist):
    t=dist/v_max
    v=dist/t
    rps=v/Circumference
    V_left= k_left*rps*k_adjustment_left
    V_right=k_right*rps*k_adjustment
    dc_left= V_left*100/3.5
    dc_right= V_right*100/3.5
    d_cycle= array.array('f',[dc_left , dc_right])
    return t, d_cycle


def steering() :
#     var_duty = duty_cycle(dist_reverse)
#     reverse_pwm(var_duty[0],var_duty[1])
     var_steer = duty_cycle(arc_right_angle/2)
     steer_left_pwm(var_steer[0],var_steer[1])
     
def steer_left_pwm(x,d_cycle):
    f1=GPIO.PWM(Backward1,1000)    
    f2=GPIO.PWM(Forward2,1000)
    dc_left=d_cycle[0]
    dc_right=d_cycle[1]
    f1.start(dc_left)
    f2.start(dc_right)
    time.sleep(x)
    GPIO.output(Forward1,GPIO.LOW)
    GPIO.output(Backward2,GPIO.LOW)
    f1.stop()
    f2.stop()
def steer_right_pwm(x,d_cycle):
    f1=GPIO.PWM(Backward1,1000)
    f2=GPIO.PWM(Forward2,1000)
    dc_left=d_cycle[0]
    dc_right=d_cycle[1]
    f1.start(dc_left)
    f2.start(dc_right)
    time.sleep(x)    
    GPIO.output(Forward1,GPIO.LOW)
    GPIO.output(Backward2,GPIO.LOW)
    f1.stop()
    f2.stop() 
def forward_pwm(x,d_cycle):
    f1=GPIO.PWM(Forward1,1000)
    f2=GPIO.PWM(Forward2,1000)
    dc_left=d_cycle[0]
    dc_right=d_cycle[1]
    f1.start(dc_left)
    f2.start(dc_right)
    time.sleep(x)
    GPIO.output(Backward1,GPIO.LOW)
    GPIO.output(Backward2,GPIO.LOW)
    f1.stop()
    f2.stop()

def reverse_pwm(x,d_cycle):
    f1=GPIO.PWM(Backward1,1000)
    f2=GPIO.PWM(Backward2,1000)
    dc_left=d_cycle[0]
    dc_right=d_cycle[1]
    f1.start(dc_left)
    f2.start(dc_right)
    #GPIO.output(Forward1,GPIO.HIGH) 
    #GPIO.output(Forward2,GPIO.HIGH)
    print("Moving Reverse")
    time.sleep(x)
    GPIO.output(Forward1,GPIO.LOW)
    GPIO.output(Forward2,GPIO.LOW)
    f1.stop()
    f2.stop()
def distance():
    GPIO.output(GPIO_TRIGGER,True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER,False)
    StartTime=time.time()
    StopTime=time.time()
    while GPIO.input(GPIO_ECHO)==0:
       StartTime=time.time() 
    while GPIO.input(GPIO_ECHO)==1:
       StopTime=time.time()    
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed*34300)/2    
    return distance

def stop():
    GPIO.output(Enable1,GPIO.LOW)
    GPIO.output(Enable2,GPIO.LOW)
    
def start():
    GPIO.output(Enable1,GPIO.HIGH)
    GPIO.output(Enable2,GPIO.HIGH)
#var=duty_cycle(20)
#forward_pwm(var[0],var[1])
#var=duty_cycle(20)
#reverse_pwm(var[0],var[1])
#stop()
#start()
#steering()
while True:
    #while count < 4:
    dist_curr= distance()
    #print("distance is =%.1f cm" % dist_curr)
    #if abs(dist_pvs-dist_curr) < 1:
        #count = count+1
    #else:
        #print("Out of range")
        #dist_pvs = dist_curr
    left_obstacle=False
    right_obstacle=False
    front_obstacle=False
    direction= 0
    if dist_curr < 20:
        front_obstacle=True
        print("distance is =%.1f cm" % dist_curr)
        #time.sleep(0.1)
        stop()
        start()
        var_steer = duty_cycle(arc_right_angle/2)
        steer_left_pwm(var_steer[0],var_steer[1])
        print("Moving Left")
        dist_curr= distance()
        if dist_curr < 20:
            left_obstacle=True
            var_steer = duty_cycle(arc_right_angle)
            steer_right_pwm(var_steer[0],var_steer[1])
            print("Moving Right")
            dist_curr= distance()
            if dist_curr < 20:
                right_obstacle=True
                var_steer = duty_cycle(arc_right_angle/2)
                steer_left_pwm(var_steer[0],var_steer[1])
                stop()
                print("Stop")
                break
    else:
        var=duty_cycle(10)
        forward_pwm(var[0],var[1])
        print("motor moving forward")
    count=0   

GPIO.cleanup()
