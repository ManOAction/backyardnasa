"""
This is the test script and diary of getting the camera module to work.

For starters we're following this tutorial.
https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2

This reminded us how to to edit the config via ssh.
https://www.raspberrypi.org/documentation/configuration/camera.md


"""

from picamera import PiCamera
from time import sleep
import time

camera = PiCamera()
PictureDirectory = '/home/ubuntu/backyardnasa/images/'

def GetPic():
    camera.start_preview()
    PicturePath = PictureDirectory + 'MatildaPic_' + str(time.time()) + '_.jpg'
    sleep(5)
    camera.capture(PicturePath)
    camera.stop_preview()

pic_loop_quit = False

while pic_loop_quit != True:

    print('Want to take a picture? (y/n)')

    user_input = input()

    try:
        if user_input == 'y':
            print('Snapping a pic.')
            GetPic()

        if user_input == 'n':
            print('Exiting loop.')
            pic_loop_quit = True

    except Exception as errormessage:
        print('Problem with user input...')
        print(errormessage)
        pic_loop_quit = False
