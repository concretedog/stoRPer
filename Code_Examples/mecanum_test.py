from machine import Pin, PWM
import time

'''
This script is for testing a mecanum wheeled stoRPer build. It drives each mecanum direction in turn for 4 seconds. 

'''
SPEED = 65025
STOP = 0

RRIGHT_FORWARD_PIN = 8 # Note that you might need to swap the pin numbers over to set the motor rotation correctly depending on how you wire in your motors. 
RRIGHT_REVERSE_PIN = 9

FRIGHT_FORWARD_PIN = 10 
FRIGHT_REVERSE_PIN = 11

FLEFT_FORWARD_PIN = 12
FLEFT_REVERSE_PIN = 13

RLEFT_FORWARD_PIN = 15
RLEFT_REVERSE_PIN = 14

rright_forward = PWM(Pin(RRIGHT_FORWARD_PIN))
rright_reverse = PWM(Pin(RRIGHT_REVERSE_PIN))

fright_forward = PWM(Pin(FRIGHT_FORWARD_PIN))
fright_reverse = PWM(Pin(FRIGHT_REVERSE_PIN))

fleft_forward = PWM(Pin(FLEFT_FORWARD_PIN))
fleft_reverse = PWM(Pin(FLEFT_REVERSE_PIN))

rleft_forward = PWM(Pin(RLEFT_FORWARD_PIN))
rleft_reverse = PWM(Pin(RLEFT_REVERSE_PIN))

def spin_wheel(pwm):
        pwm.duty_u16(SPEED)
        pwm.freq(500)
        
def stop_wheel(pwm):
        pwm.duty_u16(STOP)
        pwm.freq(500)
      

while True:
    #All forward 4 seconds
    spin_wheel(rright_forward)
    spin_wheel(fright_forward)
    spin_wheel(fleft_forward)
    spin_wheel(rleft_forward)
    
    time.sleep(4)
    stop_wheel(rright_forward)
    stop_wheel(fright_forward)
    stop_wheel(fleft_forward)
    stop_wheel(rleft_forward)
    time.sleep(1)
    
    
    #All reverse 4 seconds
    spin_wheel(rright_reverse)
    spin_wheel(fright_reverse)
    spin_wheel(fleft_reverse)
    spin_wheel(rleft_reverse)
    time.sleep(4)
    stop_wheel(rright_reverse)
    stop_wheel(fright_reverse)
    stop_wheel(fleft_reverse)
    stop_wheel(rleft_reverse)
    time.sleep(1)

    #Sideways right 4 seconds
    spin_wheel(rright_reverse)
    spin_wheel(fright_forward)
    spin_wheel(fleft_forward)
    spin_wheel(rleft_reverse)
    time.sleep(4)
    stop_wheel(rright_reverse)
    stop_wheel(fright_forward)
    stop_wheel(fleft_forward)
    stop_wheel(rleft_reverse)
    time.sleep(1)
    
    #All forward 4 seconds
    spin_wheel(rright_forward)
    spin_wheel(fright_forward)
    spin_wheel(fleft_forward)
    spin_wheel(rleft_forward)
    time.sleep(4)
    stop_wheel(rright_forward)
    stop_wheel(fright_forward)
    stop_wheel(fleft_forward)
    stop_wheel(rleft_forward)
    time.sleep(1)
    
    #Sideways left 4 seconds
    spin_wheel(rright_forward)
    spin_wheel(fright_reverse)
    spin_wheel(fleft_reverse)
    spin_wheel(rleft_forward)
    time.sleep(4)
    stop_wheel(rright_forward)
    stop_wheel(fright_reverse)
    stop_wheel(fleft_reverse)
    stop_wheel(rleft_forward)
    time.sleep(1)
    
    #All reverse 4 seconds
    spin_wheel(rright_reverse)
    spin_wheel(fright_reverse)
    spin_wheel(fleft_reverse)
    spin_wheel(rleft_reverse)
    time.sleep(4)
    stop_wheel(rright_reverse)
    stop_wheel(fright_reverse)
    stop_wheel(fleft_reverse)
    stop_wheel(rleft_reverse)
    time.sleep(1)
    