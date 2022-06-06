# File: print.py // Prints text in OLED Screen

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf

#-----------------------------------------------------------------
# IMPORTANT! - CHANGE runningStatus value to True for running code
#-----------------------------------------------------------------
s
runningStatus = False
oledWidth = 128
oledHeight = 32

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)

print("I2C Addres:    "+hex(i2c.scan()[0]).upper())
print("I2C Configuration: "+str(i2c))

oledDevice = SSD1306_I2C(oledWidth, oledHeight, i2c)

oledDevice.fill(0)

oledDevice.text("SNEIA DEV", 5, 8)
oledDevice.text("TEAM :)", 5, 18)

while runningStatus == True:
    oledDevice.show()
