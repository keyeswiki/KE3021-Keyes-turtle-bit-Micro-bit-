from microbit import *
from keyes_Bit_Turtle_Car import *
import neopixel
np = neopixel.NeoPixel(pin8, 4)
bitCar = Turtle_Car_Driver()
while True:
    distance_val = 0
    distance_val = bitCar.get_distance()
    if distance_val >= 10 and distance_val <= 30:
        bitCar.motorL(1, 100)
        bitCar.motorR(1, 100)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 0, 0)
            np.show()
    if distance_val <= 6:
        bitCar.motorL(0, 100)
        bitCar.motorR(0, 100)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 255, 0)
            np.show()
    if distance_val > 6 and distance_val < 10 or distance_val > 30:
        bitCar.motorL(0, 0)
        bitCar.motorR(0, 0)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 255, 255)
            np.show()
