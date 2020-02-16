"""This is a proof of concept for GPIO pins and a centralized file for these commands.

# changelog
2019-11-24, JDL: First draft.
2020-02-15, JDL: Creating stable loops and move commands

"""

from gpiozero import Button, LED, Motor
from time import sleep
from decimal import Decimal



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
    RMotor.forward()
    LMotor.forward()
    sleep(MoveTime)
    RMotor.stop()
    LMotor.stop()
    MotorWake.off()
    print('End moving forward.')
    return True

def move_reverse(MoveTime):
    print('Moving backwards.')
    MotorWake.on()
    RMotor.backward()
    LMotor.backward()
    sleep(MoveTime)
    RMotor.stop()
    LMotor.stop()
    MotorWake.off()
    return True

def move_turnleft(MoveTime):
    print('Turning left-ish.')
    MotorWake.on()
    RMotor.forward()
    LMotor.backward()
    sleep(MoveTime)
    RMotor.stop()
    LMotor.stop()
    MotorWake.off()
    return True

def move_turn90left(NinetyDegreeTime):
    print('Turning 90 Left.')
    MotorWake.on()
    RMotor.forward()
    LMotor.backward()
    sleep(NinetyDegreeTime)
    RMotor.stop()
    LMotor.stop()
    MotorWake.off()
    return True

def move_turn90right(NinetyDegreeTime):
    print('Turning 90 Right.')
    MotorWake.on()
    LMotor.forward()
    RMotor.backward()
    sleep(NinetyDegreeTime)
    RMotor.stop()
    LMotor.stop()
    MotorWake.off()
    return True

def move_turn180right(OneEightyDegreeTime):
    print('Turning Around.')
    MotorWake.on()
    LMotor.forward()
    RMotor.backward()
    sleep(OneEightyDegreeTime)
    RMotor.stop()
    LMotor.stop()
    MotorWake.off()
    return True


# ______
# | ___ \
# | |_/ /_____   _____ _ __
# |    // _ \ \ / / _ \ '__|
# | |\ \ (_) \ V /  __/ |
# \_| \_\___/ \_/ \___|_|
#################################################

def rover_initialize():

    global RMotor, LMotor, MotorWake

    MotorWake = LED(17)
    MotorWake.off()

    #Args are GPIO Pins for forward, backward, and motor controller sleep
    LMotor = Motor(20, 21) # Motor(19, 26, 13)
    RMotor = Motor(19, 26) # Motor(20, 21, 13)

    print("""



    #############
    x for exit
    wasd keys for directional controls.
    #############

    """)

    return True


def rover_loop():

    rover_quit = False

    # Constants (move externaly to a config when you have time)
    ####################################################
    NinetyDegreeTime = '2'
    OneEightyDegreeTime = '4'

    ####################################################

    print('90 Time is set to {0}'.format(NinetyDegreeTime))
    print('180 Time is set to {0}'.format(OneEightyDegreeTime))

    while rover_quit != True:

        print('What is thy bidding, master?')
        user_input = input()

        # Core Commands
        ######################
        if user_input == 'x':
            return False

        if user_input == 'w':
            print('For how many seconds?')
            move_forward(float(input()))

        if user_input == 'a':
            print('90 Time is set to {0}'.format(NinetyDegreeTime))
            move_turn90left(float(NinetyDegreeTime))

        if user_input == 'A':
            print('For how many seconds?')
            move_turnleft(float(input()))

        if user_input == 's':
            print('For how many seconds?')
            move_reverse(float(input()))

        if user_input == 'd':
            move_turn90right(float(NinetyDegreeTime))

        if user_input == 'D':
            print('For how many seconds?')
            move_turn90right(float(input()))

        if user_input == 'c':
            print('180 Time is set to {0}'.format(OneEightyDegreeTime))
            move_turn180right(float(OneEightyDegreeTime))

        #Testing
        ######################
        if user_input == 'q':
            print('For how many seconds?')
            move_forward(float(input()))

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
