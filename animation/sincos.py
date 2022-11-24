#!/usr/bin/env python3
"""
    sincos v1 - November 2022
    Ron@ProctorCreative.com

    Scrolls a sin and cos waves.
"""
# get smarter
import math
import time
import crayons

xfactor = 0.03 # wavelength factor
width = 60 # how wide it is
framedelay = 0.04 # delay between frames in sec

def main():
    for i in range(67*10):             # do the following lots of times
        x = i * xfactor * math.pi     # set x for current iteration
        x1 = x
        y = 1 + math.cos(x)           # y = 1+sin(x) to keep results positive
        y = math.floor( y * width/2 ) # integer, based on y*width/2
        y1 = 1 + math.sin(x1)
        y1 = math.floor( y1 * width/2 )


        for j in range(width+1):        # iterating with j, because i is busy
                
            if y == j and y == y1:
                print(crayons.yellow("+"), end="")    # draw marks
            
            elif y == j:
                print(crayons.red("+"), end="")    # draw marks

            elif y1 == j:
                print(crayons.blue("+"), end="")       # draw marks

            else:
                print(" ", end="")                    # no mark condition
        print(" ")                                   # new line
        #print(" x=",round(x,3),"y=",y) #--debug
        time.sleep(framedelay)                        # pause between frames

        # print("Step:", i, " x =", x, " y = ", y)  #--debug

main()

