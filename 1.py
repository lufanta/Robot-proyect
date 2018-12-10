# from gpiozero import Robot

# robot = Robot(motor1=(int, int),motor2=(int, int))

# robot.forward() # 2 motorrak aurrerantz mugitzen dira, () artean voltajea kontrolatu. voltaje(V) handia, motorra azkar.
# robot.backward()  # 2 motorrak atzerantz mugitzen dira,  0 <= V <= 1

# robot.right() # Ezkerreko motorrak segi eta eskubikoa geratu
# robot.left() # Eskubiko motorrak segi eta ezkerrekoa geratu



import Rpi.GPIO as GPIO
from time import sleep 

GPIO.setupmode(GPIO.BOARD)

GPIO.setup(portua1, GIPO.out(), initial = 1) # Portua1 Output gisa sortzen aktibatuta
GPIO.setup(portua2, GIPO.out(), initial = 0) # Portua2 Output gisa sortzen aktibatu gabe


try:
   while True:
       GPIO.output(portua1, 1) # portua1 eko Output/a aktibatu
       sleep(5.0) # 5 segundu itxarongo ditu
       GPIO.output(portua1, 0)# portua1 eko Output/a desaktibatu
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()