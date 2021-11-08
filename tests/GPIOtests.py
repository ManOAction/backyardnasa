

from time import sleep

from gpiozero import LED, Motor


MotorWake = LED(17)
MotorWake.off()

RMotor = Motor(20, 21)

MotorWake.on()

MotorSpeed = float('.8')

RMotor.forward(MotorSpeed)
sleep(1)
MotorWake.off()


###################################################################################

# import RPi.GPIO as GPIO

# # GPIO Initialization
# GPIO.setmode (GPIO.BCM)
# GPIO.setwarnings (True)

# """
# 17 - Motor Driver Board On/Off
# 20 - RMoter Forward
# 21 - RMoter Reverse
# """

# OutputPins = [17, 20, 21]
# GPIO.setup(OutputPins, GPIO.OUT)
# GPIO.output(OutputPins, 0)  # Setting all outputs to off.


# # Turn driver on.
# GPIO.output(17, 1)

# # Turn motor forward?
# GPIO.output(20, 0)
# GPIO.output(21, 1)

# sleep(1)

# # Reset and shut off
# GPIO.output(17, 0)
# GPIO.output(20, 0)
# GPIO.output(21, 0)

# GPIO.cleanup()



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