import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(gorri, GPIO.OUT, initial = 0)
GPIO.setup(hori, GPIO.OUT, initial = 0)
GPIO.setup(urdin, GPIO.OUT, initial = 0)
gorri = 11
hori = 15
urdin = 13
koloreak = [gorri, hori, urdin]


def Denak(gorri, hori, urdin):
    GPIO.output(gorri, 1)
    sleep(1)
    GPIO.output(gorri, 0)
    GPIO.output(urdin, 1)
    sleep(1)
    GPIO.output(urdin, 0)
    GPIO.output(hori, 1)
    sleep(1)

def batAKt(x):
    GPIO.output(x, 1)

def batDesakt(y):
    GPIO.output(y, 0)

zikloKop = 1
while True:
    Denak(gorri, hori, urdin)
    sleep(3)
    batDesakt(gorri)
    batDesakt(hori)
    sleep(3)
    batdesakt(urdin)
    print("ziklo %d eginda." % (zikloKop))
    zikloKop += 1
    sleep(4)

    

