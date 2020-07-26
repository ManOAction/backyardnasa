# https://github.com/MarkAHeywood/Bluetin_Python_Echo
from Bluetin_Echo import Echo  # HCSR04 Module Uses BCM Pins!
from time import sleep

# BCM 23 & 24 are DPI 19 and 20
DistSense = Echo(23, 24)

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
