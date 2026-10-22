from machine import Pin, PWM
import time



#

L_IN1 = PWM(Pin(14)) #define pin pairs for left motor (viewing from behind Pico), if wheel rotates wrong way swap pin numbers over 
L_IN2 = PWM(Pin(15))

R_IN1 = PWM(Pin(11)) #define pin pairs for right motor, if wheel rotates wrong way swap pin numbers over 
R_IN2 = PWM(Pin(10))

for motor in (L_IN1, L_IN2, R_IN1, R_IN2):
    motor.freq(1000) #sets frequency for PWM, 1000 is decent value for N20 motors


def set_left_motor(speed):
    if speed > 0:
        L_IN1.duty_u16(speed)
        L_IN2.duty_u16(0)
    elif speed < 0:
        L_IN1.duty_u16(0)
        L_IN2.duty_u16(abs(speed)) #makes speed variable a positive integer
    else:
        L_IN1.duty_u16(0)
        L_IN2.duty_u16(0)


def set_right_motor(speed):
    if speed > 0:
        R_IN1.duty_u16(speed)
        R_IN2.duty_u16(0)
    elif speed < 0:
        R_IN1.duty_u16(0)
        R_IN2.duty_u16(abs(speed))
    else:
        R_IN1.duty_u16(0)
        R_IN2.duty_u16(0)



FORWARD_SPEED = 30000      # 0 to 65535
TURN_SPEED = 30000         # 0 to 65535


#set up some functions for forward. backwards left and right

def forward():
    set_left_motor(FORWARD_SPEED)
    set_right_motor(FORWARD_SPEED)


def backward():
    set_left_motor(-FORWARD_SPEED)
    set_right_motor(-FORWARD_SPEED)


def left():
    # Turn on the spot
    set_left_motor(-TURN_SPEED)
    set_right_motor(TURN_SPEED)


def right():
    # Turn on the spot
    set_left_motor(TURN_SPEED)
    set_right_motor(-TURN_SPEED)


def stop():
    set_left_motor(0)
    set_right_motor(0)



try: #this is the main loop. Insert functions and let them run for a period using "time.sleep(value)"

    forward() #sets function to forward
    time.sleep(1) #allows forward function to continue for 1 second
    stop() #sets stop functio

    time.sleep(0.5) #stop remains for half a second

    left() #sets function to left turn
    time.sleep(1) #left turns for 1 second.
    stop()

    time.sleep(0.5)

    forward()
    time.sleep(1)
    stop()

except KeyboardInterrupt:
    stop()      # Stop motors safely
    print("Program stopped.") 