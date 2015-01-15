from i2clibraries import i2c_lcd
from time import *
import sys

screenType = sys.argv[1]
i2cport = int(sys.argv[2])
i2cAddress = int(sys.argv[3],16)

# Configuration parameters
# I2C Address, Port, Enable pin, RW pin, RS pin, Data 4 pin, Data 5 pin, Data 6 pin, Data 7 pin, Backlight pin (optional)
lcd = i2c_lcd.i2c_lcd(i2cAddress,i2cport, 2, 1, 0, 4, 5, 6, 7, 3)

# If you want to disable the cursor, uncomment the following line
lcd.backLightOff()
