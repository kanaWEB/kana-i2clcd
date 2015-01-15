from i2clibraries import i2c_lcd
from time import * 
import sys

screenType = sys.argv[1]
i2cport = int(sys.argv[2])
i2cAddress = int(sys.argv[3],16)
line1 = sys.argv[4]
line2 = sys.argv[5]

# Configuration parameters
# I2C Address, Port, Enable pin, RW pin, RS pin, Data 4 pin, Data 5 pin, Data 6 pin, Data 7 pin, Backlight pin (optional)
lcd = i2c_lcd.i2c_lcd(i2cAddress,i2cport, 2, 1, 0, 4, 5, 6, 7, 3)
 # If you want to enable the cursor, comment the following line
lcd.command(lcd.CMD_Display_Control | lcd.OPT_Enable_Display)
lcd.backLightOn()

lcd.writeString(line1)
lcd.setPosition(2, 0) 
lcd.writeString(line2)
