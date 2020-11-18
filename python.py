#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters importp Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile



ev3 = EV3Brick()
ev3.speaker.beep()

test_motor = Motor(Port.D)
test_motor2 = Motor(Port.C)

color_sensor = ev3.ColorSensor(Port.3)

ir = InfraredSensor(Port.4)

for _ in range(5): 
    current_color = color_sensor.color

    while current_color == ev3.ColorSensor.COLOR_RED:
        ev3.Sound.speak("here is a metal!").wait()
        test_motor.on_for_degrees(37%, -90, brake=True, block=True)
        sleep(3)
        test_motor.on_for_degrees(37%, 90, brake=True, block=True)


distance = ir.value 

if distance < 15: 
        ev3.Sound.speak("here is a wet waste!").wait()
        test_motor2.on_for_degrees(37%, -90, brake=True, block=True)
        sleep(3)
        test_motor2.on_for_degrees(37%, 90, brake=True, block=True)



    
