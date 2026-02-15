from machine import I2C, Pin
import time
from lcd_w_i2c import I2cLcd

# I2C address (usually 0x27 or 0x3F)
I2C_ADDR = 0x27

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)

lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

lcd.clear()
