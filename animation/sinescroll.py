#!/usr/bin/env python3
"""
    SineScroll v1 - November 2022
    Ron@ProctorCreative.com

    Scrolls a sinewave. Kindof.
"""

import math
import time

xfactor = 0.05
width = 60


def main():
    for i in range(200):
        x = i * xfactor * math.pi
        y = 1 + math.sin(x)
        y = round( y, 2 )
        y = math.floor( y * width/2 )

        for j in range(width):
            if y == j:
                print("+", end="")
            else:
                print(" ", end="")
        print(" ")
        time.sleep(0.1)

        # print("Step:", i, " x =", x, " y = ", y)  #--debug

main()

