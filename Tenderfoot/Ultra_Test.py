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
Target_dist = 1.5
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


# Main Code
try:
	p = GPIO.PWM(MotLEn,1000)
	q = GPIO.PWM(MotREn,1000)
	#p.start(100)
	#q.start(100)
	T_start = time.time()
	T_end = 0
	Ultra_Flag = 1
	
	while 1:
		#GPIO.output(MotL, (GPIO.LOW,GPIO.HIGH))
		#GPIO.output(MotR, (GPIO.HIGH,GPIO.LOW))
		GPIO.output(UltraTrig, 0)
		time.sleep(0.1)
		GPIO.output(UltraTrig, 1)
		time.sleep(0.00001)
		GPIO.output(UltraTrig, 0)
	        while GPIO.input(UltraEcho) == 0:
			print("UltraEcho Loop1")
			pulse_start = time.time()
		while GPIO.input(UltraEcho) == 1:
			#GPIO.output(MotL, (GPIO.LOW,GPIO.HIGH))
			#GPIO.output(MotR, (GPIO.HIGH,GPIO.LOW))
			print("UltraEcho Loop2")
			pulse_End = time.time()
		pulse_duration = pulse_End - pulse_start
		Distance = round(pulse_duration*34300/2,2)
		print("UltraEcho Loop Out" + str(Distance))
		if (Distance < 20):
			p.stop()
			q.stop()
			break
	p.stop()
	q.stop()

except KeyboardInterrupt:
	p.stop()
	q.stop()
	print("Forced Interrupted.....")

GPIO.cleanup()
