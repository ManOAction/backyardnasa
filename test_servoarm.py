"""
This is the test script and diary of getting the servo hat to work.

For starters we're following this tutorial.
https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi/using-the-python-library

2021-10-31, JDL: Retry after earlier setbacks.

"""

from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16, address=0x41)  # Don't forget we moved the address.

servo_loop_quit = False

while servo_loop_quit != True:

    print('Want to move the arms? (y/n)')

    user_input = input()

    try:
        if user_input == 'y':

            user_input = input("0 or 1?")

            if int(user_input) == 0:
                ZeroArmAngle = int(input("Angle of servo 0?"))
                kit.servo[0].angle = ZeroArmAngle
            elif int(user_input) == 1:
                OneArmAngle = int(input("Angle of servo 1?"))
                kit.servo[1].angle = OneArmAngle

        if user_input == 'n':
            print('Exiting loop.')
            servo_loop_quit = True

    except Exception as errormessage:
        print('Problem with user input...')
        print(errormessage)
        servo_loop_quit = False


print("End of File")