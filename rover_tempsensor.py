from si7021 import Si7021
from time import sleep
from smbus import SMBus



sensor = Si7021(SMBus(1))
i = 0

# Why the fuck does it have a heater?

def get_temp():
    """Returns long string of temp in C. Use %.2f *F" % (a[1]*1.8 + 32) to adjust."""
    return sensor.read()[1]


def get_humid():
    """Returns long string of humidity in %. Use %.1f %%RH to format."""
    return sensor.read()[0]


# while i <= 60:
#     print("%.1f %%RH, %.1f °C" % sensor.read())
#     # sensor.heater_mA = 50
#     a = sensor.read()
#     # print(type(a))
#     # print(str(a))
#     # print("%.1f %%RH" % a[0])
#     print("%.2f *F" % (a[1]*1.8 + 32))
#     sleep(5)
#
#     # print("%.1f %%RH, %.1f °C" % sensor.read())
#     # sensor.heater_mA = 0
#     i += 1
