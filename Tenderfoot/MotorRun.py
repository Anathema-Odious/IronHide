import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

# Pins for motor driver input
MotL = (16,18)
MotR = (36,38)
MotLEn = 12
MotREn = 40

# Equations
Target_dist = 1.5
Speed = 1.5
Wheel_dia = 6.5
Wheel_peri = 3.14*Wheel_dia/100
T_target = (Target_dist/Wheel_peri)/Speed

#T_target = 2

# Initialisation
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MotL, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MotR, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MotLEn, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MotREn, GPIO.OUT, initial=GPIO.LOW)

# Main Code
try:
	p = GPIO.PWM(MotLEn,1000)
	q = GPIO.PWM(MotREn,1000)
	
	p.start(100)
	q.start(100)
	T_start = time.time()
	T_end = 0
	
	while T_end - T_start < T_target:
		GPIO.output(MotL, (GPIO.LOW,GPIO.HIGH))
		GPIO.output(MotR, (GPIO.HIGH,GPIO.LOW))
		T_end = time.time()
	p.stop()
	q.stop()



except KeyboardInterrupt:
	print("Forced Interrupted.....")

GPIO.cleanup()