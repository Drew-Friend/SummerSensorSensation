import board
import neopixel
import time
import sys

cycle = 0
rotateCheck = 0
qty = 10
firstRun = True
primary = True
leds = neopixel.NeoPixel(board.D18, qty, auto_write=False)

#Rotates between 2 colors
def rotate(colorA, colorB, length):
    global rotateCheck
    global primary
    if rotateCheck is length:
        rotateCheck = 0
    for i in range(qty):
        if i % length == 0:
            primary = not primary
        if primary:
            leds[i - rotateCheck] = colorA
        else:
            leds[i - rotateCheck] = colorB
    
    rotateCheck += 1
    leds.show()

#GAY!! fun pretty estop code
def rainbow_cycle(wait):
    while True:
        global qty
        for j in range(255):
            for i in range(qty):
                pixel_index = (i * 256 // qty) + j
                leds[i] = wheel(pixel_index & 255)
            leds.show()
            time.sleep(wait)
#Wheel is used by the rainbow to...rainbow
def wheel(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)