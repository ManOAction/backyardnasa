# backyardnasa
Robot Rover Project

#ChangeLog
2019-11-18, JDL -- First Draft
2020-02-22, JDL -- Rover Patterns, Temp Sensors, and Chat Capabilities
2020-07-25, JDL -- Starting it up again.  Stuff's broke.

#Description

We started using this tutorial.
https://projects.raspberrypi.org/en/projects/physical-computing/3

We're pretty far beyond that.   
############################################################

Currently trying to figure out I2C.
Using this tutorial.
https://www.instructables.com/id/Raspberry-Pi-I2C-Python/
Note: When it says "i2cdetect -y 0" you need to say "i2c detect -y 1"

We're using an ancient libary with docs listed here. (got to be something better)
http://wiki.erazor-zone.de/wiki:linux:python:smbus:doc

Also using this for the temp chip.
https://pypi.org/project/Si7021/

The sensor stuff works easy as pie.   The chat stuff is still sort of a mess.
I think I'm going to make it into a slack bot instead of twitter.  Twitter doesn't
like the back and forth and prohibits repeated status updates.

We're reconfiguring the Pi to enable I2C and adding it to the kernal and some
other stuff that seems complicated at this point.
###########################################################

Check Bot Secrets for API info related to Chatbots

##########################################################

Working on distance sensors.

Following this to enable the SPI bus.
https://tutorials-raspberrypi.com/infrared-distance-measurement-with-the-raspberry-pi-sharp-gp2y0a02yk0f/



Current board is loaded up on a Pi B+
pi@192.168.122.195 was the last known location
-u pi -p raspberry



# Dependencies
Developed in Python 3.6

# Diary

7/25, JDL - Starting back into it, and stuff's broke as we were mixed up between the Blinka library
  from Adafruit and the old stuff we had.  Frustrated because it was working until I patched a change.
  Locomotion is the only thing working and it only works at low voltage (<5V).  I need to find if I
  can use capacitors or something else to prevent the battery from shorting anytime I want more
  voltage from it.  Trying to start piece by piece putting things back online.
