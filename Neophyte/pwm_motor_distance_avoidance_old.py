# importing the libraries
import time
import RPi.GPIO as GPIO


def GPIO_init():
    # Setting the GPIO mode to BOARD - Physical Numbers for GPIO
    GPIO.setmode(GPIO.BOARD)

    # Setting the GPIO pins for the motors - left and right
    motor_r = [16,18,24]
    motor_l = [19,21,23]
    us_sens_trig = 13
    us_sens_echo = 15
    reset_input = 7

    # Specifying the pins as output pins
    GPIO.setup(motor_r,GPIO.OUT)
    GPIO.setup(motor_l,GPIO.OUT)
    GPIO.setup(us_sens_trig,GPIO.OUT)
    GPIO.setup(us_sens_echo,GPIO.IN)
    GPIO.setup(reset_input,GPIO.IN)

    # Initializing the value at the pins
    GPIO.output(motor_r,GPIO.LOW)
    GPIO.output(motor_l,GPIO.LOW)
    GPIO.output(us_sens_trig,GPIO.LOW)
    GPIO.output(us_sens_echo,GPIO.LOW)
    GPIO.output(reset_input,GPIO.LOW)
    return

def main_program():
    # Main Program:
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
        r.ChangeDutyCycle(50)
        print('right turn')
        time.sleep(5)
        r.ChangeDutyCycle(100)
        return 'r'
    GPIO
    def turn_left():
        l.ChangeDutyCycle(75)
        print('left turn')
        time.sleep(5)
        l.ChangeDutyCycle(100)
        return 'l'

    def get_straight(last_turn):
        if (last_turn == 'r'):
            last_turn = turn_left()
        elif (last_turn == 'l'):
            last_turn = turn_right()
            
    def start_bot():
        
        

    GPIO.output(us_sens_trig, False)
    print ("Waiting For Sensor To Settle")
    time.sleep(1)
    print("Starting the Bot")
    forward()
    time.sleep(fw_time)

    while (dist > 20):
        dist = distance_calc()
        print ("Distance:",dist,"cm")
    #    time.sleep(0.5)


    #print("turn to avoid collison")
    #
    #last_turn = turn_right()
    #get_straight(last_turn)


    print('Stopping')    

    r.stop()
    l.stop()
    return

def reset():
    if(reset ==1):
        sleep(1)
        if(reset == 1):
            main
            while(1)
                if(reset == 0)
                reset()
    elif(reset = 0):
        i=0;
        while(i<10)
        if(reset == 0):
            i++
            sleep(1)
        elif(reset ==1):
            reset()
    return
        
GPIO_init()
main_program()
    
GPIO.cleanup()
