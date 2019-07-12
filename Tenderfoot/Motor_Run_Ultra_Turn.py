import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

# Pins for motor driver input
MotL = (16,18)
MotR = (36,38)
MotLEn = 12
MotREn = 40

UltraTrig = 11
UltraEcho = 15

# Equations
# Equations
Target_dist = 100
Speed = 1.5
Wheel_dia = 6.5
Wheel_peri = 3.14*Wheel_dia/100
T_target = (Target_dist/Wheel_peri)/Speed

# Initialisation
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MotL + MotR , GPIO.OUT, initial=GPIO.LOW)
GPIO.setup((MotLEn, MotREn), GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(UltraTrig, GPIO.OUT)
GPIO.setup(UltraEcho, GPIO.IN)

Left = GPIO.PWM(MotLEn,1000)
Right = GPIO.PWM(MotREn,1000)
Dir = 0
TurnTried = 0
TurnCount = 0
TurnCountmax = 7

ObjDistanceDetectionMax = 15
ObjDistanceDetectionMin = 10
ObjDistanceDetection = ObjDistanceDetectionMax

def Forward():
    global MotL,MotR
    GPIO.output(MotL, (GPIO.LOW,GPIO.HIGH))
    GPIO.output(MotR, (GPIO.HIGH,GPIO.LOW)) 

def Reverse():
    global MotL,MotR
    GPIO.output(MotL, (GPIO.LOW,GPIO.HIGH))
    GPIO.output(MotR, (GPIO.HIGH,GPIO.LOW))

def Stright():
    global Left,Right, Dir
    Left.ChangeDutyCycle(100)
    Right.ChangeDutyCycle(100)
    Dir = 0
    
def LeftTurn():
    global Left,Right, Dir
    Left.ChangeDutyCycle(0)
    Right.ChangeDutyCycle(100)
    Dir = 1

def RightTurn():
    global Left,Right, Dir
    Left.ChangeDutyCycle(100)
    Right.ChangeDutyCycle(0) 
    Dir = 2

def Stop():
    global Left,Right
    Left.stop()
    Right.stop() 
    



# Main Code
try:

    Left.start(100)
    Right.start(100)
    T_start = time.time()
    Ultra_Flag = 1
    
    while time.time() - T_start < T_target:
        Forward()
        #if Ultra_Flag == 1:
        GPIO.output(UltraTrig, 0)
        time.sleep(0.1)
        GPIO.output(UltraTrig, 1)
        time.sleep(0.00001)
        GPIO.output(UltraTrig, 0)
        #Ultra_Flag == 2
        while GPIO.input(UltraEcho) == 0  and time.time() - T_start < T_target:
            Forward()
            #Ultra_Flag = 3
            pulse_start = time.time()
        while GPIO.input(UltraEcho) == 1 and time.time() - T_start < T_target:
            Forward()
            pulse_End = time.time()
            
        pulse_duration = pulse_End - pulse_start
        Distance = round(pulse_duration*34300/2,2)
        print("Distance : " + str(Distance) + "Turn Tried" + str(TurnTried))
        Ultra_Flag = 1
        if (Distance < ObjDistanceDetection):
            if TurnTried >= 2:	
                Stop()
                break
            if (Dir == 0):
		LeftTurn()                
                TurnTried = TurnTried + 1                    
                print("Left Turn" + str(TurnTried)) 
                TurnCount = TurnCountmax
		ObjDistanceDetection = ObjDistanceDetectionMin
            elif (Dir == 1):
		RightTurn()
                TurnTried = TurnTried + 1                    
                print("Right Turn" + str(TurnTried))    
                TurnCount = TurnCountmax
		ObjDistanceDetection = ObjDistanceDetectionMin  
              
        if TurnCount > 0 :
            TurnCount = TurnCount -1
        if TurnCount == 0:
            print("Stright")
            Stright()
            TurnTried = 0
	    ObjDistanceDetection = ObjDistanceDetectionMax

except KeyboardInterrupt:
    print("Forced Interrupted.....")

GPIO.cleanup()
