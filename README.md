# backyardnasa
Robot Rover Project

#ChangeLog
2019-11-18, JDL -- First Draft
2020-02-22, JDL -- Rover Patterns, Temp Sensors, and Chat Capabilities

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

Twitter is fussy about repeatable status updates.   Switching to Slack for right now.

Check Bot Secrets for API info

##########################################################

Working on distance sensors.

Following this to enable the SPI bus.
https://tutorials-raspberrypi.com/infrared-distance-measurement-with-the-raspberry-pi-sharp-gp2y0a02yk0f/



Current board is loaded up on a Pi B+
pi@192.168.122.195 was the last known location
-u pi -p raspberry



# Dependencies
Developed in Python 3.6+

# rover
gpiozero  # Used to handle the GPIO pins.

# twitterbot
twython # Twitterbot library

#TODO

We have it running in simple patterns and looping through a rover command interface.

We need to add eyes so it learns object avoidance.

Also get twitter bot up and running.
