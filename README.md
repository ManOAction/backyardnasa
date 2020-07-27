# Backyard NASA Rover Project
I figured making a robot rover that lived on its own somewhere and sent pictures of
rocks back to me couldn't be that hard if the gubberment folks at NASA could do it.

Her name is Matilda, and this is her story.

We started using this tutorial.
https://projects.raspberrypi.org/en/projects/physical-computing/3

# ChangeLog
2020-07-26, JDL -- Motors, Atmo, Sonic, and Magna systems are all working.
2020-07-25, JDL -- Starting it up again.  Stuff's broke.
2020-02-22, JDL -- Rover Patterns, Temp Sensors, and Chat Capabilities
2019-11-18, JDL -- First Draft

# TODO
Heading Based Turning: Use the magnetometer to turn in degree increments rather
    than time based increments.

Twin Sonic Sensors: Sensors need to be mounted over tracks and facing down to look
    cliffs and drop offs.

Chatbot: The chatbot needs to be put in the cloud and have it occasionally request
    things of Matilda probably through processes independent of the rover loop.

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

# Diary
##########################################################

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
