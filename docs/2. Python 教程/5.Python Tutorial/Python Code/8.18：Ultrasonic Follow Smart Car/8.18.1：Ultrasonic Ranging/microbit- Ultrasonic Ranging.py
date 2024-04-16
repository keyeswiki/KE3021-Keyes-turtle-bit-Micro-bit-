from microbit import *
from keyes_Bit_Turtle_Car import *
bitCar = Turtle_Car_Driver()
import music
tune = ["C4:4"]
distance_val = 0
while True:
    i = 0
    distance_val = bitCar.get_distance()
    print("distance:", distance_val)
    if distance_val < 10:
        while i < 1:
            music.play(tune)
            sleep(200)
            music.play(tune)
            sleep(200)
            i += 1
