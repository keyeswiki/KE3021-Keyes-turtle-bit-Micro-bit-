from microbit import *
val_LL = 0
while True:
    val_LL = pin14.read_digital()
    print("digital signal:", val_LL)
    sleep(200)
