import random
import time
from threading import Thread
from GPIO import RPI.gpio as RPI

RPI.


class WaitForUserInput(Thread):
    def run(self):
        # your original code
        a = random.randint(0, 9)
        ans = 2 * a
        q = ""
        q = int(input("Calculate 2 * %d\n" % a))
        # added these lines of code from my side :)
        if q == ans:
            print('You did it!')


def print_message():
    print("You can do it")
    time.sleep(3)


while True:
    waiting_for_input = WaitForUserInput()
    waiting_for_input.start()

    while waiting_for_input.is_alive():
        print_message()
