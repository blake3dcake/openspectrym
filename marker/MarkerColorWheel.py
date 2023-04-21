from machine import Pin, PWM
from time import sleep
import uasyncio
import itertools

Rpin = Pin(16, Pin.OUT)
Gpin = Pin(17, Pin.OUT)
Bpin = Pin(18, Pin.OUT)
Rpwm = machine.PWM(Rpin)
Gpwm = machine.PWM(Gpin)
Bpwm = machine.PWM(Bpin)
Rpwm.freq(50)
Gpwm.freq(50)
Bpwm.freq(50)
servo_min_duty = 1200
servo_max_duty = 7700
#the time it takes to loop through one color rotation
#20mins
Time = (20 * 60)
#Time/3 colors
Tick = (Time/3)

#rgb values
#equivalent to (1,0,0),(0,1,0),(0,0,1)
#the numbers are different because they account for the variation in each servo as well as the rotational position of each 'markerholder'
#you should edit these values to find the 'set' and 'reset' positions of the markers. Alternatively you could rotate the position of the 'markerholders'
ColorWheel = [(12,44,39),(30,26,39),(30,44,21),]

#starting color of the color wheel
#programmed to loop through
#0=red 2=green 4=blue
start_idx = 0
color_iter = itertools.cycle(ColorWheel[start_idx:])

def set_servo_angle(angle,servo):
    duty_cycle = int(servo_min_duty + (angle/180) * (servo_max_duty - servo_min_duty))
    servo.duty_u16(duty_cycle)
    
def setcolor():
    while True:
        color = next(color_iter)
        set_servo_angle(color[0],Rpwm)
        set_servo_angle(color[1],Gpwm)
        set_servo_angle(color[2],Bpwm)
        sleep(Tick)
        
#resets the servo position so the markers are not touching the filament
#these values are specific to each individual servo
#use this function to expierementally determine what values corespond with the the equivalent range of motion of your servo
def reset():
    set_servo_angle(30,Rpwm)
    set_servo_angle(44,Gpwm)
    set_servo_angle(39,Bpwm)
    sleep(1)
 
reset() 
setcolor()