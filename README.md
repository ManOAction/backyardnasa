# Backyard NASA Rover Project
I figured making a robot rover that lived on its own somewhere and sent pictures of
rocks back to me couldn't be that hard if the gubberment folks at NASA could do it.

Her name is Matilda, and this is her story.

We started using this tutorial.
https://projects.raspberrypi.org/en/projects/physical-computing/3

# ChangeLog
2020-12-27, JDL -- Updating diary and writing new roadmap for 2021
2020-07-26, JDL -- Motors, Atmo, Sonic, and Magna systems are all working.
2020-07-25, JDL -- Starting it up again.  Stuff's broke.
2020-02-22, JDL -- Rover Patterns, Temp Sensors, and Chat Capabilities
2019-11-18, JDL -- First Draft

# TODO
  Now being tracked in the "Current Roadmap Section"

# Other Ideas
Automatic Hard Iron Offset Recalibration: Use the magnet calibrator logic in the middle of
    360 turning to reset and reassign offset variables.


# Changes from Stock Raspian Setup
############################################################

We're reconfiguring the Pi to enable I2C and adding it to the kernal.
https://www.instructables.com/id/Raspberry-Pi-I2C-Python/
Note: When it says "i2cdetect -y 0" you need to say "i2c detect -y 1"

We're using an ancient library with docs listed here. (got to be something better)
http://wiki.erazor-zone.de/wiki:linux:python:smbus:doc

Following this to enable the SPI bus.
https://tutorials-raspberrypi.com/infrared-distance-measurement-with-the-raspberry-pi-sharp-gp2y0a02yk0f/

# Misc Thoughts
###########################################################

Check Bot Secrets for API info related to Chatbots

Use i2cdetect -y 1 to confirm I2C connections

Current board is loaded up on a Pi B+
pi@192.168.122.195 was the last known location
-u pi -p raspberry

##########################################################

# Broad Roadmap
##########################################################

Phase I: Basic Capabilities:
  - Pictures of Objects
  - Geofencing
  - Talking to Slack Channel  
  - Passive Charging and Voltage Checking

Phase II: Initial Backyard Trials
  - Success after multiple days of continuous operation achieved

Phase III: Scale to Pasture Size
  - Build to "coffee table" size

Phase IV: Profit?

# Current Roadmap (Newly drafted on 12/27)
##########################################################

Separate Motor Power Supply
  - This means having the computer run on a self contained system away from the
  drive motors.

  - Twin Sonic Sensors (HCSR04) for the left and right bumpers.

  - Functioning camera module that talks to a social account (slack?)

  - Update 3D printed housing for sensors, Pi, and batteries.

  - Capable of autonomous functioning until batteries deplete themselves.

# Diary
##########################################################

12/27, JDL - After lying dormant for months, matilda boots and runs fine, but the motors and power issue
  remain an issue.   I'm going to pursue using a NiMH battery to power the motors with a MOSFET in between
  to turn the battery on and off.  It looks like charging NiMH is a bit of a pain, but we're going to move
  forward with it since it's what we've got.   Passive charging/recharging may be a feature that is a long
  ways down the road.  We may as well get it to function long enough to deplete it's batteries before we try
  to learn how to recharge it.

7/26, JDL - I got tripped up on BCM/DPI pin numbering and it took a long time to fix.  Everything's working
  right now.  I'm going to clean up the codebase and then move on to a new feature to add.

7/26, JDL - This is dumb.  After looking at the official CircuitPython libraries for the HCSR04, they
  just have a poor feature set compared to this guy's custom one.  https://github.com/MarkAHeywood/Bluetin_Python_Echo
  I'm switching back to using it.

7/25, JDL - Starting back into it, and stuff's broke as we were mixed up between the Blinka library
  from Adafruit and the old stuff we had.  Frustrated because it was working until I patched a change.
  Locomotion is the only thing working and it only works at low voltage (<5V).  I need to find if I
  can use capacitors or something else to prevent the battery from shorting anytime I want more
  voltage from it.  Trying to start piece by piece putting things back online.
