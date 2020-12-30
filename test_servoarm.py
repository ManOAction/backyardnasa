"""
This is the test script and diary of getting the servo hat to work.

For starters we're following this tutorial.
https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi/attach-and-test-the-hat

2020-12-29, JDL: First Draft

"""

from smbus import SMBus
import board
import busio
import Adafruit_PCA9685

import adafruit_fxos8700
import adafruit_fxas21002c


i2c = busio.I2C(board.SCL, board.SDA)

fxos = adafruit_fxos8700.FXOS8700(i2c)
fxas = adafruit_fxas21002c.FXAS21002C(i2c)

hat = Adafruit_PCA9685.PCA9685(i2c)

print('End of File.  Yeay?')