import board
import busio
import adafruit_fxos8700
import adafruit_fxas21002c
import time
from math import atan2, degrees


i2c = busio.I2C(board.SCL, board.SDA)
fxos = adafruit_fxos8700.FXOS8700(i2c)
fxas = adafruit_fxas21002c.FXAS21002C(i2c)

mag_offset_x = float('25')
mag_offset_y = float('-28')
mag_offset_z = float('-85')

try:
    while True:
        # print('Acceleration (m/s^2): ({0:0.2f},{1:0.2f},{2:0.2f})'.format(*fxos.accelerometer))
        mag_x, mag_y, mag_z = fxos.magnetometer
        mag_x = mag_x - mag_offset_x
        mag_y = mag_y - mag_offset_y
        mag_z = mag_z - mag_offset_z
        heading = degrees(atan2(mag_y, mag_x))
        if heading < 0:
            heading += 360
        # print('Magnetometer (uTesla): ({0:0.2f},{1:0.2f},{2:0.2f})'.format(mag_x, mag_y, mag_z))
        print('Heading: {0:0.2f}'.format(heading))
        # print('Gyroscope (radians/s): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*fxas.gyroscope))
        # print(fxas.gyroscope)

        time.sleep(1)
except KeyboardInterrupt:
    pass

# try:
#     while True:
#         gyro_x, gyro_y, gyro_z = fxas.gyroscope
#         print('Gyroscope (radians/s): ({0:0.3f},  {1:0.3f},  {2:0.3f})'.format(gyro_x, gyro_y, gyro_z))
#         time.sleep(1.0)
# except KeyboardInterrupt:
#     pass

print("""\nExiting...""")
