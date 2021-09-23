import time, board, neopixel, random
pixel_pin = board.IO12
num_pixels = 11
pixel = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3)
while True:
    for i in range(0, 11):
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        pixel[i] = (color)
        time.sleep(1)


