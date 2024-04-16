from microbit import *
from keyes_Bit_Turtle_Car import *
bitCar = Turtle_Car_Driver()
ledr = 0
ledg = 0
ledb = 0
while True:
    for index in range(51):
        bitCar.headlights_Left(ledr, 0, 0)
        bitCar.headlights_Right(ledr, 0, 0)
        sleep(100)
        ledr += 5
    for index in range(51):
        bitCar.headlights_Left(ledr, 0, 0)
        bitCar.headlights_Right(ledr, 0, 0)
        sleep(100)
        ledr += -5
    for index in range(51):
        bitCar.headlights_Left(0, ledg, 0)
        bitCar.headlights_Right(0, ledg, 0)
        sleep(100)
        ledg += 5
    for index in range(51):
        bitCar.headlights_Left(0, ledg, 0)
        bitCar.headlights_Right(0, ledg, 0)
        sleep(100)
        ledg += -5
    for index in range(51):
        bitCar.headlights_Left(0, 0, ledb)
        bitCar.headlights_Right(0, 0, ledb)
        sleep(100)
        ledb += 5
    for index in range(51):
        bitCar.headlights_Left(0, 0, ledb)
        bitCar.headlights_Right(0, 0, ledb)
        sleep(100)
        ledb += -5
