from machine import I2C, Pin
from lcd_w_i2c import I2cLcd
import time

I2C_ADDR = 0x27   # Change to 0x3F if needed
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

message = "   Hello from Pico   "

while True:
    for i in range(len(message) - 15):
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr(message[i:i+16])
        time.sleep(0.3)
