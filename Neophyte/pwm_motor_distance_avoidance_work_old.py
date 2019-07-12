# importing the libraries
import time
import RPi.GPIO as GPIO


#def GPIO_init():
#    # Setting the GPIO mode to BOARD - Physical Numbers for GPIO
#    GPIO.setmode(GPIO.BOARD)
#
#    # Setting the GPIO pins for the motors - left and right
#    motor_r = [16,18,24]
#    motor_l = [19,21,23]
#    us_sens_trig = 13
#    us_sens_echo = 15
#    reset = 7
#
#    # Specifying the pins as output pins
#    GPIO.setup(motor_r,GPIO.OUT)
#    GPIO.setup(motor_l,GPIO.OUT)
#    GPIO.setup(us_sens_trig,GPIO.OUT)
#    GPIO.setup(us_sens_echo,GPIO.IN)
#    GPIO.setup(reset,GPIO.IN)
#
#    # Initializing the value at the pins
#    GPIO.output(motor_r,GPIO.LOW)
#    GPIO.output(motor_l,GPIO.LOW)
#    GPIO.output(us_sens_trig,GPIO.LOW)
#    print("GPIO Setting has been initialized")
#    return

def main_program():
    # Main Program:
    print("main called")
    # PWM for the left and right motors
    frequency = 1000
    r = GPIO.PWM(motor_r[2],frequency)
    l = GPIO.PWM(motor_l[2],frequency)

    dc_r = 100
    dc_l = 100

    # Calibration:

    offset = 15

    dc_r = dc_l - offset

    r.start(dc_r)
    l.start(dc_l)

    # Setting distance to a default high value
    dist = 1000
    fw_time = 0
    last_turn = ''

    def forward():
        GPIO.output(16,GPIO.HIGH)    
        GPIO.output(18,GPIO.LOW)
        GPIO.output(19,GPIO.HIGH)
        GPIO.output(21,GPIO.LOW)
        print("Going Forward")
        return

    def distance_calc():
        GPIO.output(us_sens_trig, True)
        time.sleep(0.00001)
        GPIO.output(us_sens_trig, False)
        while GPIO.input(us_sens_echo)==0:
            pulse_start = time.time()
        while GPIO.input(us_sens_echo)==1:
            pulse_end = time.time()      
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration*17150
        distance = round(distance, 2)
        return distance

    def turn_right():
        r.ChangeDutyCycle(0)
        print('right turn')
        time.sleep(1)
        r.ChangeDutyCycle(dc_r)
        return 'r'
 
    def turn_left():
        l.ChangeDutyCycle(0)
        print('left turn')
        time.sleep(2)
        l.ChangeDutyCycle(dc_l)
        return 'l'

    def get_straight(last_turn):
        if (last_turn == 'r'):
            last_turn = turn_left()
        elif (last_turn == 'l'):
            last_turn = turn_right()
       

    GPIO.output(us_sens_trig, False)
    print ("Waiting For Sensor To Settle")
    time.sleep(1)
    print("Starting the Bot")
    forward()
    time.sleep(fw_time)

    while (dist > 20):
        dist = distance_calc()
        print ("Distance:",dist,"cm")
    
    turn_right()
    turn_left()


    print('Stopping')    

    r.stop()
    l.stop()
    return

def ex():
    GPIO.cleanup()
    print("Exiting")
    return 0

def reset_func():
    flag = 1
    while (1==flag):
        if(GPIO.input(reset) ==1):
            print("b")
            time.sleep(1)
            if(GPIO.input(reset) == 1):
                main_program()
                while(1):
                    print("d")
                    if(GPIO.input(reset) == 0):
                        print("e")
                        time.sleep(1)
                        if(GPIO.input(reset) == 0):
                            print("f")
                            break
        elif(GPIO.input(reset) == 0):
            print("c")
            i=0
            while(i<10):
                if(GPIO.input(reset) == 0):
                    i = i + 1
                    time.sleep(1)
                    print("waited for ", i, " sec")
                    if (9==i):
                        flag = ex()
                        break
                elif(GPIO.input(reset) ==1):
                    i = 10
    return
        
# Setting the GPIO mode to BOARD - Physical Numbers for GPIO
GPIO.setmode(GPIO.BOARD)

# Setting the GPIO pins for the motors - left and right
motor_r = [16,18,24]
motor_l = [19,21,23]
us_sens_trig = 13
us_sens_echo = 15
reset = 7

# Specifying the pins as output pins
GPIO.setup(motor_r,GPIO.OUT)
GPIO.setup(motor_l,GPIO.OUT)
GPIO.setup(us_sens_trig,GPIO.OUT)
GPIO.setup(us_sens_echo,GPIO.IN)
GPIO.setup(reset,GPIO.IN)

# Initializing the value at the pins
GPIO.output(motor_r,GPIO.LOW)
GPIO.output(motor_l,GPIO.LOW)
GPIO.output(us_sens_trig,GPIO.LOW)
print("GPIO Setting has been initialized")
reset_func()
