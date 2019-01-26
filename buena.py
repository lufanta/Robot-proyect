import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.board)

Motor1A = 16
Motor1B = 18
Motor1E = 22
motorA = [Motor1A, Motor1B, Motor1E]

Motor2A = 23
Motor2B = 21
Motor2E = 19
motorB = [Motor2A, Motor2B, Motor2E]


GPIO.setup(motorA, GPIO.OUT)
GPIO.setup(motorB, GPIO.OUT)

#Aurrera
GPIO.output(Motor1A, 1)
GPIO.output(Motor1B, 0)
GPIO.output(Motor1E, 1)

GPIO.output(Motor2A, 1)
GPIO.output(Motor2B, 0)
GPIO.output(Motor2E, 1)
