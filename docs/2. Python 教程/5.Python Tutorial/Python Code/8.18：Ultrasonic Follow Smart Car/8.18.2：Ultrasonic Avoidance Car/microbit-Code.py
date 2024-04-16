from microbit import *
from keyes_Bit_Turtle_Car import *
bitCar = Turtle_Car_Driver()
distance_val = 0

while True:

    distance_val = bitCar.get_distance()

    if distance_val > 15:
        bitCar.motorL(1, 200)
        bitCar.motorR(1, 200)
        bitCar.headlights_Left(0, 255, 0)
        bitCar.headlights_Right(0, 255, 0)
    else:
        bitCar.motorL(0, 150)
        bitCar.motorR(1, 200)
        bitCar.headlights_Left(0, 0, 255)
        bitCar.headlights_Right(0, 0, 255)
