"""This is a proof of concept for GPIO pins and a centralized file for these commands.

# imports
from gpiozero import Button, LED
from time import sleep

# changelog
2019-11-24, JDL: First draft.

"""


from gpiozero import Button, LED
from time import sleep


def blink_the_light():
    """This will blink the light until the button is pressed."""

    f_exit = 0

    print('Press button again to turn off light.')

    while f_exit < 1:
        light.on()
        sleep(.25)
        light.off()
        sleep(.25)
        if button.is_pressed:
            f_exit = 1
            print('Shutting off the light.')

    return True


# Using GPIO pins #20 & 21
button = Button(20)
light = LED(21)

while True:
    print('Press button to turn light on.')
    button.wait_for_press()
    blink_the_light()
    sleep(1)



# Don't know how we exited the previous loop...
print('End of File.')
