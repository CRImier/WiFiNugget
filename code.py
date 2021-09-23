## CircuitPython Neopixel Test for the Wi-Fi Nugget by Kody Kinzie @Skickar 2021
import time, board, neopixel, random   # Import modules for delays, pins, neopixel, & random number generator

pixel_pin = board.IO12    # Specify the pin that the neopixel is connected to (GPIO 12)
num_pixels = 11; delay = .1   # Set number of neopixels & delay between color changes in seconds
pixel = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3)   # Create neopixel and set brightness to 30%

def SetAll(color):   # Define function with one input (color we want to set)
    for i in range(0, num_pixels):   # Addressing all 11 neopixels in a loop
        pixel[i] = (color)   # Set all neopixels a color

def RandomChase():   # Run this loop forever
    for i in range(0, 11):   # Addressing all 11 neopixels in a loop
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))   # Create a random color
        pixel[i] = (color)   # Set the neopixel to the random color
        pixel[(i-1)] = (0,0,0)   # Turn the neopixel before the random colored one off
        time.sleep(delay)   # Make a brief delay before running the loop again

#SetAll((0, 0, 255))   # Set all pixels to a single color without delay
#while True: RandomChase()   # Create a random color chase animation
