from hw import * # getting all the things from the hardware module so we can access them easily
import random
import network

show_compressed(cutie_c) # showing the "cutie" image

np = get_neopixels(1) # only one Neopixel connected

# disabling both network interfaces by default
# reenable the ones you need
sta = network.WLAN(network.STA_IF)
sta.active(False)
ap = network.WLAN(network.AP_IF)
ap.active(False)

# some "animations"

def schroedinger():
    while True:
        show_compressed(cutie_c)
        show_compressed(dead_c)

def caramelldansen():
    while True:
        np[0] = [random.getrandbits(6) for i in range(3)]
        np.write()
        sleep(0.27)
        lcd.flip(not lcd.flip_en, update=False)
        show_compressed(cutie_c)
        np[0] = [random.getrandbits(6) for i in range(3)]
        np.write()
        sleep(0.27)
        show_compressed(nyaa_c)
