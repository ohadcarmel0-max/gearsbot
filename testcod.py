#!/usr/bin/env python3

# Import the necessary libraries
import time
import math
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor.virtual import *

# Create the sensors and motors objects
motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
left_motor = motorA
right_motor = motorB
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)

spkr = Sound()
btn = Button()
radio = Radio()
obtr = ObjectTracker()

color_sensor_in1 = ColorSensor(INPUT_1)
ultrasonic_sensor_in2 = UltrasonicSensor(INPUT_2)
ultrasonic_sensor_in3 = UltrasonicSensor(INPUT_3)
ultrasonic_sensor_in4 = UltrasonicSensor(INPUT_4)
gyro_sensor_in5 = GyroSensor(INPUT_5)

motorC = LargeMotor(OUTPUT_C) # Magnet

# Here is where your code starts

# Describe this function...
def forward():
    while ultrasonic_sensor_in2.distance_centimeters > 25:
        tank_drive.on(40, 40)
    tank_drive.off(brake=True)

# Describe this function...
def turn_right():
    gyro_sensor_in5.reset()
    while gyro_sensor_in5.angle <= 90:
        tank_drive.on(80, 0)
    tank_drive.off(brake=True)
    while gyro_sensor_in5.angle != 90:
        tank_drive.on(0, 2)
    tank_drive.off(brake=True)

# Describe this function...
def turn_left():
    gyro_sensor_in5.reset()
    while gyro_sensor_in5.angle >= -90:
        tank_drive.on(0, 80)
    tank_drive.off(brake=True)
    while gyro_sensor_in5.angle != -90:
        tank_drive.on(2, 0)
    tank_drive.off(brake=True)


while not color_sensor_in1.rgb[0]:
    forward()
    if ultrasonic_sensor_in3.distance_centimeters > ultrasonic_sensor_in4.distance_centimeters:
        turn_left()
    else:
        turn_right()
