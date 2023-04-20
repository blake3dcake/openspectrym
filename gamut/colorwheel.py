import uasyncio
import itertools
from machine import Pin
from time import sleep

Rstep = Pin(27, Pin.OUT)
Rdir = Pin(26, Pin.OUT)
Gstep = Pin(21, Pin.OUT)
Gdir = Pin(20, Pin.OUT)
Bstep = Pin(17, Pin.OUT)
Bdir = Pin(16, Pin.OUT)
Rrate = 0
Grate = 0
Brate = 0

#rgb color intensity values
#for example (.7,.3,0) is the same as red=70%, green=30%, blue=0%
ColorWheel = [
    (1,0,0),
    (.7,.3,0),
    (.5,.5,0),
    (.3,.7,0),
    (0,1,0),
    (0,.7,.3),
    (0,.5,.5),
    (0,.3,.7),
    (0,0,1),
    (.3,0,.7),
    (.5,0,.5),
    (.7,0,.3),
]

#motor direction
#controls DIR pin on A4988 motor drivers
#useful for priming pumps
Rdir.value(0)
Gdir.value(0)
Bdir.value(0)

#set color starting position
#control individual pumps to prime them before a print
#0=red 4=green 8=blue
start_idx = 0
color_iter = itertools.chain(ColorWheel[start_idx:], ColorWheel[:start_idx])

#time to complete one cycle through the color wheel
#(time * 60seconds)
Time = (240 * 60)
Tick = (Time/12)

#set MaxFlow of the pumps
#smaller value = higher flow
#MaxFlow = .001 is max speed (use max speed to prime the pumps at the start of a print)
#MaxFlow = 1 is a good place to start
MaxFlow = 1
FlowRate = 1/MaxFlow

async def SetColor():
    global Rrate, Grate, Brate
    while True:
        color = next(color_iter)
        Rrate = round(color[0]*FlowRate,2)
        Grate = round(color[1]*FlowRate,2)
        Brate = round(color[2]*FlowRate,2)
        print(Rrate,Grate,Brate)
        await uasyncio.sleep(Tick)
        
async def StepRed():
    global Rrate
    while True:
        if Rrate != 0:
            Rstep.value(1)
            await uasyncio.sleep(round((1/Rrate),2))
            print("r",round(Rrate,2))
            Rstep.value(0)
            await uasyncio.sleep_ms(1)
        else:
            await uasyncio.sleep_ms(1)
        
async def StepGreen():
    global Grate
    while True:
        if Grate != 0:
            Gstep.value(1)
            await uasyncio.sleep(round((1/Grate),2))
            print("g",round(Grate,2))
            Gstep.value(0)
            await uasyncio.sleep_ms(1)
        else:
            await uasyncio.sleep_ms(1)        
        
def StepBlue():
    global Brate
    while True:
        if Brate != 0:
            Bstep.value(1)
            await uasyncio.sleep(round((1/Brate),2))
            print("b",round(Brate,2))
            Bstep.value(0)
            await uasyncio.sleep_ms(1)
        else:
            await uasyncio.sleep_ms(1)

async def main():
    task1 = uasyncio.create_task(SetColor())
    task2 = uasyncio.create_task(StepRed())
    task3 = uasyncio.create_task(StepGreen())
    task4 = uasyncio.create_task(StepBlue())
    await uasyncio.gather(task1, task2, task3, task4)

uasyncio.run(main())

