"""This is a proof of concept for GPIO pins.

# imports
from gpiozero import LED
from time import sleep

# changelog
2019-11-24, JDL: First draft.

"""


from gpiozero import LED
from time import sleep

# Using GPIO pin #21
dualmotors = LED(12)

# Blinking That Light
# while True:
print('Starting Motors.')
dualmotors.on()
sleep(5)
dualmotors.off()
sleep(.25)


# Don't know how we exited the previous loop...
print('End of File.')
