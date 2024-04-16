from microbit import *
from keyes_Bit_Turtle_Car import *
import neopixel
bitCar = Turtle_Car_Driver()
np = neopixel.NeoPixel(pin8, 4)
display.show(Image.HAPPY)
val_LL = 0
val_CC = 0
val_RR = 0
while True:
    val_LL = pin14.read_digital()
    val_CC = pin15.read_digital()
    val_RR = pin16.read_digital()
    for pixel_id1 in range(0, len(np)):
        np[pixel_id1] = (255, 100, 100)
        np.show()
    if val_LL == 0 and val_CC == 1 and val_RR == 0:
        bitCar.motorL(1, 60)
        bitCar.motorR(1, 60)
    elif val_LL == 0 and val_CC == 1 and val_RR == 1:
        bitCar.motorL(1, 60)
        bitCar.motorR(1, 60)
    elif val_LL == 1 and val_CC == 0 and val_RR == 1:
        bitCar.motorL(1, 60)
        bitCar.motorR(1, 60)
    elif val_LL == 1 and val_CC == 1 and val_RR == 0:
        bitCar.motorL(1, 60)
        bitCar.motorR(1, 60)
    elif val_LL == 1 and val_CC == 1 and val_RR == 1:
        bitCar.motorL(1, 60)
        bitCar.motorR(1, 60)
    elif val_LL == 1 and val_CC == 0 and val_RR == 0:
        bitCar.motorL(0, 30)
        bitCar.motorR(1, 80)
    elif val_LL == 0 and val_CC == 0 and val_RR == 1:
        bitCar.motorL(1, 80)
        bitCar.motorR(0, 30)
    else:
        bitCar.motorL(0, 0)
        bitCar.motorR(0, 0)
