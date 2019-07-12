import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
MotorR1 = 16
MotorR2 = 18
MotorRen = 24
MotorL1 = 19
MotorL2 = 21
MotorLen = 23
TRIG = 13
ECHO = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(MotorR1,GPIO.OUT)
GPIO.setup(MotorR2,GPIO.OUT)
GPIO.setup(MotorRen,GPIO.OUT)
GPIO.output(MotorR1,GPIO.LOW)
GPIO.output(MotorR2,GPIO.LOW)
r=GPIO.PWM(MotorRen,1000)
GPIO.setup(MotorL1,GPIO.OUT)
GPIO.setup(MotorL2,GPIO.OUT)
GPIO.setup(MotorLen,GPIO.OUT)
GPIO.output(MotorL1,GPIO.LOW)
GPIO.output(MotorL2,GPIO.LOW)
l=GPIO.PWM(MotorLen,1000)
l.start(100)
r.start(83)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
distance = 1000

GPIO.output(TRIG, False)
print ("Waiting For Sensor To Settle")
time.sleep(1)
print("motor_spec")
GPIO.output(MotorR1,GPIO.HIGH)
GPIO.output(MotorR2,GPIO.LOW)
GPIO.output(MotorL1,GPIO.HIGH)
GPIO.output(MotorL2,GPIO.LOW)

while (distance > 20):
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()      
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration*17150
    distance = round(distance, 2)
    print ("Distance:",distance,"cm")  
    #time.sleep(0.5)
print("stop or crashhhh")    
r.stop()
l.stop()
GPIO.cleanup()