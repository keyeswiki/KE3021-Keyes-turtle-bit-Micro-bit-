#from microbit import pin1, pin2, sleep, i2c
from microbit import *
import ustruct
from time import sleep_us, ticks_us
distance = 0

class Turtle_Car_Driver(object):
    def __init__(self):
        self.add = 0x47
        i2c.write(self.add, bytearray([0x00, 0x00]), repeat=False)
        self.set_all_pwm(0, 0)
        i2c.write(self.add, bytearray([0x01, 0x04]), repeat=False)
        i2c.write(self.add, bytearray([0x00, 0x01]), repeat=False)
        sleep(5)
        i2c.write(self.add, bytearray([0x00]), repeat=False)
        mode1s = i2c.read(self.add, 1)
        #mode1 = ustruct.unpack('<H', mode1)[0]
        mode1 = mode1s[0]
        mode1 = mode1 & ~0x10
        i2c.write(self.add, bytearray([0x00, mode1]), repeat=False)
        sleep(5)

    def set_pwm(self, channel, on, off):
        if on is None or off is None:
            i2c.writ(self.add, bytearray([0x06+4*channel]), repeat=False)
            data = i2c.read(self.add, 4)
            return ustruct.unpack('<HH', data)
        i2c.write(self.add, bytearray([0x06+4*channel, on & 0xFF]), repeat=False)
        i2c.write(self.add, bytearray([0x07+4*channel, on >> 8]), repeat=False)
        i2c.write(self.add, bytearray([0x08+4*channel, off & 0xFF]), repeat=False)
        i2c.write(self.add, bytearray([0x09+4*channel, off >> 8]), repeat=False)

    def set_all_pwm(self, on, off):
        i2c.write(self.add, bytearray([0xFA, on & 0xFF]), repeat=False)
        i2c.write(self.add, bytearray([0xFB, on >> 8]), repeat=False)
        i2c.write(self.add, bytearray([0xFC, off & 0xFF]), repeat=False)
        i2c.write(self.add, bytearray([0xFD, off >> 8]), repeat=False)

    def map(self, value, fromLow, fromHigh, toLow, toHigh):
        return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

    '''
    def constrain(self, Value, Low, High):
        if Value <= Low:
            return Low
        elif Value >= High:
            return High
        else:
            return Value
    '''

    def headlights_Right(self, R, G, B):
        R = int((R/255)*4095)
        G = int((G/255)*4095)
        B = int((B/255)*4095)
        self.set_pwm(7, 0, R)
        self.set_pwm(6, 0, G)
        self.set_pwm(8, 0, B)

    def headlights_Left(self, R, G, B):
        R = int((R/255)*4095)
        G = int((G/255)*4095)
        B = int((B/255)*4095)
        self.set_pwm(9, 0, R)
        self.set_pwm(10, 0, G)
        self.set_pwm(11, 0, B)

    def motorL(self, stateL, left1):
        left = int(self.map(left1, 0, 255, 0, 4095))
        if (stateL == 1):
            self.set_pwm(2, 4096, 0)
            self.set_pwm(1, 0, 0)
            self.set_pwm(0, 0, left)
        if (stateL == 0):
            self.set_pwm(2, 0, 0)
            self.set_pwm(1, 4096, 0)
            self.set_pwm(0, 0, left)

    def motorR(self, stateR, right1):
        right = int(self.map(right1, 0, 255, 0, 4095))
        if (stateR == 1):
            self.set_pwm(3, 4096, 0)
            self.set_pwm(4, 0, 0)
            self.set_pwm(5, 0, right)
        if (stateR == 0):
            self.set_pwm(3, 0, 0)
            self.set_pwm(4, 4096, 0)
            self.set_pwm(5, 0, right)

    def get_distance(self):
        global distance
        for i in range(10):
            pin1.write_digital(1)
            sleep_us(15)
            pin1.write_digital(0)
            if pin2.read_digital() == 1:
                ts = ticks_us()
                while pin2.read_digital() == 1:
                    pass
                te = ticks_us()
                tc = te - ts
                distance = (tc*170)*0.0001
                if(distance > 800):
                    distance = 0
        return round(distance, 2)

