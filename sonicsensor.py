# https://github.com/MarkAHeywood/Bluetin_Python_Echo
from Bluetin_Echo import Echo  # HCSR04 Module
from time import sleep


DistSense = Echo(19, 20)

def report_dist():
    samples = 4
    try:
        while True:
            d = DistSense.read('cm', samples)
            print(d, 'cm')
            sleep(.5)
    except KeyboardInterrupt:
        pass


report_dist()

DistSense.stop()

print('End Of File.')
