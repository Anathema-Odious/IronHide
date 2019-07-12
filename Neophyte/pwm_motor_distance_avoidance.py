# importing the libraries
import time
import RPi.GPIO as GPIO

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
    
    def forward_bot():
        GPIO.output(16,GPIO.HIGH)    
        GPIO.output(18,GPIO.LOW)
        GPIO.output(19,GPIO.HIGH)
        GPIO.output(21,GPIO.LOW)
        print("Bot Going Forward")
        return

    def forward(t):
        GPIO.output(16,GPIO.HIGH)    
        GPIO.output(18,GPIO.LOW)
        GPIO.output(19,GPIO.HIGH)
        GPIO.output(21,GPIO.LOW)
        print("Going Forward")
        time.sleep(t)
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
        #print ("Distance:",distance,"cm")
        obstacle = (distance <= 20)
        #print ("Obstacle Present:",obstacle)
        return obstacle

    def turn_right(tr):
        GPIO.output(16,GPIO.LOW)    
        GPIO.output(18,GPIO.HIGH)
        r.ChangeDutyCycle(dc_r)
        l.ChangeDutyCycle(0)
        print('right turn')
        time.sleep(tr)
        GPIO.output(16,GPIO.HIGH)    
        GPIO.output(18,GPIO.LOW)
        l.ChangeDutyCycle(dc_l)
        return
 
    def turn_left(tl):
#        GPIO.output(19,GPIO.LOW)    
#        GPIO.output(21,GPIO.HIGH)
        r.ChangeDutyCycle(dc_r)
        l.ChangeDutyCycle(0)
        print('left turn')
        time.sleep(tl)
#        GPIO.output(19,GPIO.HIGH)
#        GPIO.output(21,GPIO.LOW)
        l.ChangeDutyCycle(dc_l)
        return
    
    def turn_l_180():        
        turn_left(2.0)
        return

    def get_straight(last_turn):
        if (last_turn == 'r'):
            last_turn = turn_left()
        elif (last_turn == 'l'):
            last_turn = turn_right()
        return

    def stop():
        r.ChangeDutyCycle(0)
        l.ChangeDutyCycle(0)
        return
    
    def analyze_obstacle():
        obs_r = 0
        obs_l = 0
        stop()
        time.sleep(0.5)
        turn_right(1.2)
        stop()
        time.sleep(0.5)
        obstacle  = distance_calc()
        if (obstacle):
            obs_r = 1
        turn_l_180()
        obstacle  = distance_calc()
        if (obstacle):
            obs_l = 1
        if (1==obs_l and 1==obs_r):
            print("AO: 0")
            return(0)
        if (0==obs_l and 1==obs_r):
            print("AO: 1 - obstacle on right")
            return(1)
        if (1==obs_l and 0==obs_r):
            turn_l_180()
            return(2)
        if (0==obs_l and 0==obs_r):
            return(3)
        
#    def take_action(ana_out):
#        if (0==ana_out):
#            stop()
#            print("Sorry entered a dead-end: Parking")
#            return
#        elif(1==ana_out):
#            #forward(1)
#            return
#        elif(2==ana_out):
#            #forward(1)
#            return
#        elif(3==ana_out):
#            #forward(1)
#            return
            
           
    

    GPIO.output(us_sens_trig, False)
    print ("Waiting For Sensor To Settle")
    time.sleep(1)
    print("Starting the Bot")
    forward_bot()
    st = 0
    #time.sleep(fw_time)
    while(st!= 1):
        obstacle = 0
        while (obstacle == 0):
            obstacle = distance_calc()
        ao = analyze_obstacle()
        print("st loop")
    #    take_action(ao)
        if (0==ao):
                stop()
                print("Sorry entered a dead-end: Parking")
                st = 1
        elif(1==ao):
                forward_bot()
        elif(2==ao):
                forward_bot()
        elif(3==ao):
                forward_bot()
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
main_program()
#reset_func()
