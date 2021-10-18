from machine import Pin, I2C
from neopixel import NeoPixel
from time import sleep
import framebuf
import gc

import sh1106

# Wemos pins - for our and our users' convenience
D0 = const(16)
D1 = const(5)
D2 = const(4)
D3 = const(0)
D4 = const(2)
D5 = const(14)
D6 = const(12)
D7 = const(13)
D8 = const(15)

# I2C and screen

i2c = I2C(scl=Pin(D1), sda=Pin(D2), freq=400000) # I2C object on pins D1 an dD2
lcd = sh1106.SH1106_I2C(128, 64, i2c, None, 0x3c, rotate=180)  # SH1106 display on I2C 0x3C, rotated
# screen init
lcd.sleep(False)  # Turn on the display
lcd.fill(0)  # Erase display

# Neopixel

numPixels = 1  # How many pixels are attached to the nugget? If just the built in display, put 1
pin = Pin(D8, Pin.OUT)   # set GPIO15 to output to drive NeoPixels

def get_neopixels(count):
    return NeoPixel(pin, count)   # create NeoPixel driver on GPIO15 for all neopixels

# Buttons

down  = green  = Pin(D3, Pin.IN, Pin.PULL_UP)  # down is green
up    = red    = Pin(D6, Pin.IN, Pin.PULL_UP)  # up is red
left  = blue   = Pin(D7, Pin.IN, Pin.PULL_UP)  # left is blue
right = yellow = Pin(D5, Pin.IN, Pin.PULL_UP)  # right is yellow

# Screen image decompression

def unpack(packed_data):
    """
    Decompresses image data using a very simple algorithm described in 'pack'.
    Returns a bytearray.
    """
    i = 0 # index for the unpacked bytearray element that we're currently on
    # checking the compression format version, for future compatibility in case this algo changes significantly
    if packed_data[0] != 1:
        print("Don't know how to decompress this image, format version:", packed_data[0])
        return None
    # pre-creating a bytearray of the length we need, initially filled with zeroes
    # to avoid creating too many useless objects and wasting memory as we unpack
    unpacked_data = bytearray(packed_data[1])
    for element in packed_data[2:]: # need to skip two elements - version and length
        if isinstance(element, int): # just an int, simply putting it into the bytearray
            unpacked_data[i] = element
            i += 1
        else:
            value, count = element
            if value == 0: # small optimization
                # skipping zero-filling since bytearrays are pre-filled with zeroes
                i += count
            else:
                for _ in range(count):
                    unpacked_data[i] = value
                    i += 1
    return unpacked_data

# Showing compressed images

def show_compressed(packed_data):
    data = unpack(packed_data)
    fb = framebuf.FrameBuffer(data, 124, 64, framebuf.MONO_VLSB)
    lcd.fill(0)
    lcd.blit(fb, 0, 0)
    lcd.show()
    del data
    del fb
    gc.collect()

cutie_c = [1, 992, [0, 253], 192, [224, 2], 112, 56, 60, [28, 2], [14, 9], [28, 2], 56, 120, 240, 224, 192, 128, [0, 63], 192, 224, 240, 120, 60, 28, [14, 3], [7, 7], 6, [14, 2], 28, 60, 56, 240, 224, 192, 128, [0, 7], 240, 252, 255, 7, 1, [0, 11], 32, [248, 2], [252, 2], 248, 112, [0, 2], 1, 3, 31, 254, 248, 128, [0, 57], 224, 252, 255, 7, 1, [0, 12], 120, [252, 4], 120, [0, 3], 1, 7, 255, 254, 240, [0, 5], 15, 127, 255, 224, 128, [0, 13], [1, 3], [0, 5], 192, 240, 255, 63, 1, [0, 26], 112, [248, 7], 112, [0, 22], 3, 31, 127, 240, 192, 128, [0, 19], 128, 192, 240, 255, 63, 7, [0, 7], 1, 3, 7, 15, 30, 60, 56, 48, [112, 2], [96, 2], [224, 3], 96, [112, 3], [56, 2], 28, 14, 15, 7, 1, [0, 21], 24, 120, 240, 192, 128, [0, 5], 1, 3, 255, 3, 1, [0, 5], 128, 192, 240, 120, 24, [0, 17], 1, 3, 7, 15, 30, 28, [56, 3], [112, 7], 48, [56, 2], 28, 30, 14, 7, 3, 1, [0, 60], 1, 3, 7, 6, 14, [12, 4], 15, 12, 8, [12, 2], [6, 2], [3, 2], 1, [0, 175]]
dead_c = [1, 992, [0, 137], 1, 3, 15, 31, 127, 255, 254, 248, 240, 192, 128, [0, 4], 128, 192, 240, 252, 254, 255, 63, 31, 7, 3, [0, 50], 1, 3, 15, 31, 127, 255, 254, 248, 240, 192, 128, [0, 4], 128, 192, 240, 252, 254, 255, 63, 31, 7, 3, [0, 30], 3, 7, 31, 191, 255, 254, [248, 2], 254, 255, 31, 15, 7, 1, [0, 61], 3, 7, 31, 191, 255, 254, [248, 2], 254, 255, 31, 15, 7, 1, [0, 33], 128, 224, 240, 252, 254, 127, 31, 15, 3, 7, 31, 127, 255, 254, 248, 240, 192, 128, [0, 57], 128, 224, 240, 252, 254, 127, 31, 15, 3, 7, 31, 127, 255, 254, 248, 240, 192, 128, [0, 27], 32, 56, 60, [63, 3], 15, 3, 1, [0, 8], 3, 15, 31, [63, 2], 62, 60, 48, 32, [0, 20], 112, [248, 7], 112, [0, 20], 32, 56, 60, [63, 3], 15, 3, 1, [0, 8], 3, 15, 31, [63, 2], 62, 60, 48, 32, [0, 61], 24, 120, 240, 192, 128, [0, 5], 1, 3, 255, 3, 1, [0, 5], 128, 192, 240, 120, 24, [0, 102], 1, 3, 7, 6, 14, [12, 4], 15, 12, 8, [12, 2], [6, 2], [3, 2], 1, [0, 175]]
nyaa_c = [1, 992, [0, 270], 128, 224, [248, 3], 224, 192, [0, 68], 128, 224, [248, 3], 224, 192, [0, 37], 128, 224, 240, 252, 254, 127, 31, 15, 3, 7, 31, 127, 255, 254, 248, 240, 192, 128, [0, 57], 128, 224, 240, 252, 254, 127, 31, 15, 3, 7, 31, 127, 255, 254, 248, 240, 192, 128, [0, 27], 32, 56, 60, [63, 3], 15, 3, 1, [0, 8], 3, 15, 31, [63, 2], 62, 60, 48, 32, [0, 20], 112, [248, 7], 112, [0, 20], 32, 56, 60, [63, 3], 15, 3, 1, [0, 8], 3, 15, 31, [63, 2], 62, 60, 48, 32, [0, 61], 24, 120, 240, 192, 128, [0, 5], 1, 3, 255, 3, 1, [0, 5], 128, 192, 240, 120, 24, [0, 102], 1, 3, 7, 6, 14, [12, 4], 15, 12, 8, [12, 2], [6, 2], [3, 2], 1, [0, 175]]
