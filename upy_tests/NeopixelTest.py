## uPy Neopixel Test for the Wi-Fi Nugget
## Based on CircuitPython Neopixel Test for the Wi-Fi Nugget by Kody Kinzie @Skickar 2021
import random
from time import sleep
from machine import Pin
from neopixel import NeoPixel

def randint(upper):
    # upy only has `random.getrandbits()` so this will have to do
    # counting amount of bits in `upper`
    num_bits = 0
    _upper = upper
    while _upper:
        _upper = _upper >> 1
        num_bits += 1
    # generating random integers in a loop until we get one that's less than `upper`
    ri = upper + 1 # initial number for the 'while' loop to start
    while ri >= upper:
        ri = random.getrandbits(num_bits)
    # got it!
    return ri


num_pixels = 1 # Set number of neopixels
delay = 0.1 # Set delay between color changes in seconds
pin = Pin(15, Pin.OUT)   # set GPIO15 to output to drive NeoPixels
pixel = NeoPixel(pin, num_pixels)

def SetAll(color):   # Define function with one input (color we want to set)
    for i in range(0, num_pixels):   # Addressing all neopixels in a loop
        pixel[i] = (color)   # Set all neopixels a color

def RandomChase():   # Run this loop forever
    for i in range(0, num_pixels):   # Addressing all neopixels in a loop
        color = (randint(255), randint(255), randint(255))   # Create a random color
        pixel[i] = (color)   # Set the neopixel to the random color
        sleep(delay)   # Make a brief delay before running the loop again
    pixel.write()
