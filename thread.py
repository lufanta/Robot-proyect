import random
import time
from threading import Thread
from RPi.GPIO import GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(gorri, GPIO.OUT, initial = 0)
GPIO.setup(hori, GPIO.OUT, initial = 0)
GPIO.setup(urdin, GPIO.OUT, initial = 0)


gorri = input(int("Gorriaren tokia")
hori = input(int("horiaren tokia")
urdin = input(int("urdinaren tokia")

koloreak [gorri, hori,urdin]

class WaitForUserInput(Thread, koloreak):
    def run(self,koloreak):
        #Main on Thread
        GPIO.output(gorri, 1)
        sleep(1)
        GPIO.output(gorri, 0)
        GPIO.output(urdin, 1)
        sleep(1)
        GPIO.output(urdin, 0)
        GPIO.output(hori, 1)
        sleep(1)

def main(koloreak):
         number1 = random.randint(0, 9)
         number2 = random.randint(0, 9)
         result = number1 * number2
         erantzuna = int(input("Zenbat da {} * {}").value(number1, number1)))
         if erantzuna == result:
             GPIO.output(urdina, 1)
             sleep(2)
             GPIO.output(urdina, 0)
        else:
             GPIO.output(gorri, 1)
             sleep(2)
             GPIO.output(gorri, 0)
              
              
while True:
    waiting_for_input = WaitForUserInput()
    waiting_for_input.start()

    while waiting_for_input.is_alive():
        main()
