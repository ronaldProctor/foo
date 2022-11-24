#!/usr/bin/env python3
"""
    SineScroll v1 - November 2022
    Ron@ProctorCreative.com

    Scrolls a sinewave.
"""
# get smarter
import math
import time
import crayons

xfactor = 0.05 # wavelength factor
width = 60 # how wide it is
framedelay = 0.04 # delay between frames in sec

def main():
    for i in range(200):              # do the following 200 times
        x = i * xfactor * math.pi     # set x for current iteration
        y = 1 + math.cos(x)           # y = 1+sin(x) to keep results positive
        y = math.floor( y * width/2 ) # integer, based on y*width/2


        for j in range(width):        # iterating with j, because i is busy
            if y == j:
                print(crayons.yellow("+"), end="")    # mark it if it's on

            else:
                print(" ", end="")    # leave it blank if not
        print(" ")                     # new line
        time.sleep(framedelay)               # pause between frames

        # print("Step:", i, " x =", x, " y = ", y)  #--debug

main()

