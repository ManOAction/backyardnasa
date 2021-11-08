

from time import sleep

# from gpiozero import LED, Motor

# MotorWake = LED(17)
# MotorWake.off()

# RMotor = Motor(20, 21)

# MotorWake.on()

# MotorSpeed = float('.8')

# RMotor.forward(MotorSpeed)
# sleep(1)
# MotorWake.off()

# from Bluetin_Echo import Echo  # Uses BCM Pins.

# LeftEye = Echo(23, 24)
# RightEye = Echo(17, 27)

# def report_dist():
#     samples = 3
#     i = 0
#     while i < 20:
#         d = LeftEye.read('cm', samples)
#         print('Left: ', d, 'cm')
#         d = RightEye.read('cm', samples)
#         print('Right: ', d, 'cm')
#         sleep(.25)
#         i += 1

#     return True

# report_dist()


from busio import I2C
import board
from adafruit_si7021 import SI7021
i2c = I2C(board.SCL, board.SDA)






















##################################################################################

# These are the Blinka tools for managing the related sensors
# from gpiozero import LED, Motor
# from busio import I2C
# import board
# # from adafruit_fxos8700 import FXOS8700  # accelo / magnetometer
# # from adafruit_fxas21002c import FXAS21002C  # gyro
# # from adafruit_si7021 import SI7021  # temp and humidiy
# from Bluetin_Echo import Echo  # HCSR04 Module Uses BCM Pins!


# MoveTime = float('1')  # float('1.109')
# MotorSpeed = float('.8')


# Starting over after moving to ubuntu.

# Initializing I2C for sensors
# i2c = I2C(board.SCL, board.SDA)

# Initializing Gyro and Magnetometer
# Accelo = FXOS8700(i2c)
# Gyro = FXAS21002C(i2c)

# Initializing Atmo Sensor
# AtmoSensor = SI7021(i2c)

# Annoyingly it looks like the HCSR04 Libary uses DPI Pin Numbering instead
# of Broadcom.  Check here https://pinout.xyz/pinout/pin18_gpio24
# Read about speed of sound calibration in doc
# BCM 23 & 24 are DPI 19 and 20
# LeftEye = Echo(23, 24)
# RightEye = Echo(17, 27)

# MotorWake = LED(17)
# MotorWake.off()

# # Args are GPIO Pins for forward, backward, and motor controller sleep
# RMotor = Motor(20, 21)  # Motor(19, 26, 13)
# LMotor = Motor(19, 26)  # Motor(20, 21, 13)


# print('Moving forward.')
# MotorWake.on()
# RMotor.forward(MotorSpeed)
# LMotor.forward(MotorSpeed)
# sleep(MoveTime)
# RMotor.stop()
# LMotor.stop()
# MotorWake.off()
# print('End moving forward.')

print('End of File')