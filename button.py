"""This is a proof of concept for GPIO pins.

# imports
from gpiozero import Button
from time import sleep

# changelog
2019-11-24, JDL: First draft.

"""


from gpiozero import Button
from time import sleep

# Using GPIO pin #21
button = Button(20)

# Blinking That Light
print('Waiting for button to be pushed.')
button.wait_for_press()
print('You pushed me.  Exiting File.')


# Don't know how we exited the previous loop...
print('End of File.')
