from microbit import *
val_LL = 0
val_CC = 0
val_RR = 0
while True:
    val_LL = pin14.read_digital()
    val_CC = pin15.read_digital()
    val_RR = pin16.read_digital()
    if val_LL == 0 and val_CC == 1 and val_RR == 1:
        display.show(Image("00009:""00009:""00009:""00009:""00009"))
    elif val_LL == 1 and val_CC == 0 and val_RR == 1:
        display.show(Image("00900:""00900:""00900:""00900:""00900"))
    elif val_LL == 1 and val_CC == 1 and val_RR == 0:
        display.show(Image("90000:""90000:""90000:""90000:""90000"))
    elif val_LL == 0 and val_CC == 0 and val_RR == 1:
        display.show(Image.HEART_SMALL)
    elif val_LL == 0 and val_CC == 1 and val_RR == 0:
        display.show(Image.YES)
    elif val_LL == 1 and val_CC == 0 and val_RR == 0:
        display.show(Image.NO)
    elif val_LL == 1 and val_CC == 1 and val_RR == 1:
        display.show(Image.SAD)
    else:
        display.show(Image.HEART)
