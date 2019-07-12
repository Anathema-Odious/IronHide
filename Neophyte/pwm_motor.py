import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
MotorR1 = 16
MotorR2 = 18
MotorRen = 24
MotorL1 = 19
MotorL2 = 21
MotorLen = 23


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
r.start(100)
l.start(89.85)

#print("\n")
#print("Bakwaas Right.....")
#print("\n")    

GPIO.output(MotorR1,GPIO.HIGH)
GPIO.output(MotorR2,GPIO.LOW)
GPIO.output(MotorL1,GPIO.HIGH)
GPIO.output(MotorL2,GPIO.LOW)
time.sleep(6.1)

#r.ChangeDutyCycle(75)
#print("75")
#time.sleep(5)
#r.ChangeDutyCycle(100)
#print("100")
#time.sleep(5)
#
#
#
#print("\n")
#print("Bakwaas Left.....")
#print("\n")    
#    
#print("50")
#GPIO.output(MotorL1,GPIO.HIGH)
#GPIO.output(MotorL2,GPIO.LOW)
#time.sleep(5)
#
#l.ChangeDutyCycle(75)
#print("75")
#time.sleep(5)
#l.ChangeDutyCycle(100)
#print("100")
#time.sleep(5)

r.stop()
l.stop()
GPIO.cleanup()