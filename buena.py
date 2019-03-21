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
GPIO.output(Motor1A, True)
GPIO.output(Motor1B, False)
GPIO.output(Motor1E, True)

GPIO.output(Motor2A, True)
GPIO.output(Motor2B, False)
GPIO.output(Motor2E, True)
