"""This is a proof of concept for GPIO pins and a centralized file for these commands.

# changelog
2019-11-24, JDL: First draft.
2020-02-15, JDL: Creating stable loops and move commands

# Dependencies
We're using the circuit python blinka library because we're using so many adafruit breakout
boards.  https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi
pip3 install adafruit-blinka

"""

from gpiozero import Button, LED, Motor
from time import sleep


# These are the Blinka tools for managing the related sensors
from busio import I2C
import board
import adafruit_fxos8700  # accelo / magnetometer
import adafruit_fxas21002c  # gyro
import adafruit_hcsr04  # sonic sensor
from adafruit_si7021 import SI7021  # temp and humidiy

# Constants (move externaly to a config when you have time)
####################################################
NinetyDegreeTime = float('.65')
OneEightyDegreeTime = float('1.3')
RightTurnMod = float('1')  # float('1.109')
MotorSpeed = float('1')


####################################################

# Sensing
####################################################

def report_atmo():
    print("The Temperature: %0.1f F" % (AtmoSensor.temperature*(9/5)+32))
    print("Humidity: %0.1f %%" % AtmoSensor.relative_humidity)

    return True

def report_dist():
    samples = 3
    i = 0
    while i < 40:
        d = DistSense.read('cm', samples)
        print(d, 'cm')
        sleep(.25)
        i += 1




# ___  ___                                    _
# |  \/  |                                   | |
# | .  . | _____   _____ _ __ ___   ___ _ __ | |_
# | |\/| |/ _ \ \ / / _ \ '_ ` _ \ / _ \ '_ \| __|
# | |  | | (_) \ V /  __/ | | | | |  __/ | | | |_
# \_|  |_/\___/ \_/ \___|_| |_| |_|\___|_| |_|\__|
#################################################


def move_forward(MoveTime):
    print('Moving forward.')
    MotorWake.on()
    RMotor.forward(MotorSpeed)
    LMotor.forward(MotorSpeed)
    sleep(MoveTime)
    RMotor.stop()
    LMotor.stop()
    MotorWake.off()
    print('End moving forward.')
    return True

def move_reverse(MoveTime):
    print('Moving backwards.')
    MotorWake.on()
    RMotor.backward(MotorSpeed)
    LMotor.backward(MotorSpeed)
    sleep(MoveTime)
    RMotor.stop()
    LMotor.stop()
    MotorWake.off()
    return True

def move_turnleft(MoveTime):
    print('Turning left.')
    MotorWake.on()
    RMotor.forward(MotorSpeed)
    LMotor.backward(MotorSpeed)
    sleep(MoveTime)
    RMotor.stop()
    LMotor.stop()
    MotorWake.off()
    return True

def move_turnright(MoveTime):
    print('Turning right.')
    MotorWake.on()
    RMotor.backward(MotorSpeed)
    LMotor.forward(MotorSpeed)
    sleep(MoveTime*RightTurnMod)
    RMotor.stop()
    LMotor.stop()
    MotorWake.off()
    return True


# Patterns
##############################################
def move_box(MoveTime):
    move_forward(MoveTime)
    move_turnleft(NinetyDegreeTime)
    move_forward(MoveTime)
    move_turnleft(NinetyDegreeTime)
    move_forward(MoveTime)
    move_turnleft(NinetyDegreeTime)
    move_forward(MoveTime)
    move_turnleft(NinetyDegreeTime)

def move_hunt():
    objectfound = 0
    d = DistSense.read('cm', 3)
    while objectfound < 3:
        MotorWake.on()
        RMotor.forward(float(MotorSpeed*.5))
        LMotor.forward(float(MotorSpeed*.5))
        print('Moving Forward...')
        d = 0

        while d == 0 or d > 30:
            d = DistSense.read('cm', 3)
            print(d, 'cm Loop')

        RMotor.stop()
        LMotor.stop()
        MotorWake.off()
        print('Object Found!')
        objectfound += 1
        sleep(3)
        print('Reversing...')
        move_reverse(float(1))
        sleep(3)
        print('Turning...')
        move_turnright(float(1))
        sleep(3)



# ______
# | ___ \
# | |_/ /_____   _____ _ __
# |    // _ \ \ / / _ \ '__|
# | |\ \ (_) \ V /  __/ |
# \_| \_\___/ \_/ \___|_|
#################################################

def rover_initialize():

    global RMotor, LMotor, MotorWake, AtmoSensor, DistSense, Accelo, Gyro

    # Initializing I2C for sensors
    i2c = I2C(board.SCL, board.SDA)

    # Initializing Gyro and Magnetometer
    Accelo = adafruit_fxos8700.FXOS8700(i2c)
    Gyro = adafruit_fxas21002c.FXAS21002C(i2c)

    # Initializing Atmo Sensor
    AtmoSensor = SI7021(i2c)

    # Annoyingly it looks like the HCSR04 Libary uses DPI Pin Numbering instead
    # of Broadcom.  Check here https://pinout.xyz/pinout/pin18_gpio24
    # BCM 23 & 24 are DPI 19 and 20
    # DistSense = adafruit_hcsr04.HCSR04(trigger_pin=board.D19, echo_pin=board.D20)  # Read about speed of sound calibration in docs

    MotorWake = LED(17)
    MotorWake.off()

    # Args are GPIO Pins for forward, backward, and motor controller sleep
    LMotor = Motor(20, 21)  # Motor(19, 26, 13)
    RMotor = Motor(19, 26)  # Motor(20, 21, 13)

    print("""

    #############
    x for exit
    wasd keys for directional controls. Capital letters for custom turns.
    c for 180
    b for Box Pattern

    r for Atmospheric Report
    p for Distance Sensing Mode
    h for Hunt Mode
    #############

    """)

    return True


def rover_loop():

    rover_quit = False

    while rover_quit != True:

        print('What is thy bidding, master?')
        user_input = input()

        try:
            # Core Commands
            ######################
            if user_input == 'x':
                return False

            if user_input == 'w':
                print('For how many seconds?')
                move_forward(float(input()))

            if user_input == 'a':
                print('90 Time is set to {0}'.format(NinetyDegreeTime))
                move_turnleft(float(NinetyDegreeTime))

            if user_input == 'A':
                print('For how many seconds?')
                move_turnleft(float(input()))

            if user_input == 's':
                print('For how many seconds?')
                move_reverse(float(input()))

            if user_input == 'd':
                move_turnright(float(NinetyDegreeTime))

            if user_input == 'D':
                print('For how many seconds?')
                move_turnright(float(input()))

            if user_input == 'c':
                print('180 Time is set to {0}'.format(OneEightyDegreeTime))
                move_turnleft(float(OneEightyDegreeTime))

            if user_input == 'b':
                print('How big a box?')
                move_box(float(input()))

            if user_input == 'r':
                report_atmo()

            if user_input == 'p':
                report_dist()

            if user_input == 'h':
                move_hunt()

        except Exception as errormessage:
            print('Problem with user input...')
            print(errormessage)


        rover_quit = False

    return True


#  _____                    _
# |  ___|                  | |
# | |____  _____  ___ _   _| |_ ___
# |  __\ \/ / _ \/ __| | | | __/ _ \
# | |___>  <  __/ (__| |_| | ||  __/
# \____/_/\_\___|\___|\__,_|\__\___|
################################################################################

if __name__ == '__main__':
    rover_initialize()
    rover_loop()

print('I think we\'re done here.')
