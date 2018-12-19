# from gpiozero import Robot

# robot = Robot(motor1=(int, int),motor2=(int, int))

# robot.forward() # 2 motorrak aurrerantz mugitzen dira, () artean voltajea kontrolatu. voltaje(V) handia, motorra azkar.
# robot.backward()  # 2 motorrak atzerantz mugitzen dira,  0 <= V <= 1

# robot.right() # Ezkerreko motorrak segi eta eskubikoa geratu
# robot.left() # Eskubiko motorrak segi eta ezkerrekoa geratu


#
#import Rpi.GPIO as GPIO
#from time import sleep 

#GPIO.setupmode(GPIO.BOARD)

#GPIO.setup(portua1, GIPO.out(), initial = 1) # Portua1 Output gisa sortzen aktibatuta
#GPIO.setup(portua2, GIPO.out(), initial = 0) # Portua2 Output gisa sortzen aktibatu gabe

#try:
 #GPIO.output(portua1, 1) # portua1 eko Output/a aktibatu
  #     sleep(5.0) # 5 segundu itxarongo ditu
   #    GPIO.output(portua1, 0)# portua1 eko Output/a desaktibatu
#except KeyboardInterrupt:
 #   GPIO.cleanup()


import Rpi.GPIO as GPIO
import time

GPIO.setupmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT)# PWM-rako erabilgarriak diren bakarrak 18, 12, 13 19
GPIO.setup(12, GPIO.OUT)

m1 = 18
GPIO.pwm(18, 40) #Motorraren portua eta bere frekuentzia jartzen. GPIO.PWM(Portua, frekuentzia)
m2 = 12
GPIO.pwn(12, 40)
motorrak[m1, m2]

# motorren "duty cicle" = 50. %50 eko potentziarekin = 3.3V / 2
motorrak.start(50)
x = 0

try:
    while True:
        if x != 100:
         x = 75
         motorrak.ChangeDutyCicle(x) # Motorren "duty cicle" = 75. %75 eko potentzian = 3.3V * 0,75
         x += 1 # Motorren "duty cicle"-a ziklo bakoitzena 1 igoko da. Beraz, abiadura gero eta azkarrago
        else:
         x = 0 
finally:
    cleanup()
