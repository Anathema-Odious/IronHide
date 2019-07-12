import sys
import RPi.GPIO as GPIO
import time
import array
GPIO.setwarnings(False)
GPIO.cleanup()
time.sleep(1)
#Ultrasonic Sensor
GPIO_TRIGGER=32
GPIO_ECHO=40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
distance = 100
GPIO.output(GPIO_TRIGGER,False)
print("Distance measure about to start")
time.sleep(1)

while True:
    GPIO.output(GPIO_TRIGGER,True)
    #print("Trigger High")
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER,False)
    #print("Trigger Low")
    StartTime=time.time()
    StopTime=time.time()
#    time.sleep(0.01)
    echo_in=GPIO.input(GPIO_ECHO)
    #print("Echo Voltage =%.2f Volts" % echo_in)
    object_det=(echo_in==1.0)
    #print(bool(object_det))
    StTime = time.time()
    while GPIO.input(GPIO_ECHO)==0:
        #print("Echo Low") 
        StartTime=time.time()
        #StpTime = time.time()
        #if StpTime -StTime > 0.01:
          #break
    while GPIO.input(GPIO_ECHO)==1:
        #print("Echo High")
        StopTime=time.time()
        
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed*34300)/2
    print("distance in cm = ",distance)
    #if distance < 3:
       # print("distance is =%.1f cm" % distance)
       # time.sleep(1)
    #else:
     #  print("Out of range") 
GPIO.cleanup()
