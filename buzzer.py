"""This is a proof of concept for GPIO pins.

# imports
from gpiozero import Buzzer
from time import sleep

# changelog
2019-11-24, JDL: First draft.

"""


from gpiozero import Buzzer
from time import sleep

# Using GPIO pin #26
buzz = Buzzer(26)

# # Blinking That Light
# while True:
buzz.on()
sleep(.5)
buzz.off()
# sleep(.25)


# Don't know how we exited the previous loop...
print('End of File.')
