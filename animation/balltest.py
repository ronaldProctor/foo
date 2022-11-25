#!/usr/bin/env

#  animation testing
#  ron@proctorcreative.com
#  
#  redraws screen with series of frames from an art file

# get smarter
import os
import math
import time

# art text file
arttext = "test.txt"
# how many frames in loop
framecount = 8
# how many frames to draw
framesout = 100
# set frame delay (sec)
framedelay = 0.1
# define lines per frame
linesperframe = 12

def main():

    with open( arttext, "r" ) as artfile:
 
        artlines = artfile.readlines()

        for i in range( framesout ):
        
            j = int( math.floor( i % framecount ) * linesperframe )  # j's modulo to framecount
            # print(j)  #--debug

            k = int( j + linesperframe )  # last line for current frame

            currentframe = artlines[ j:k ]  # all pixels for current frame

            os.system( "clear" )  # blank terminal screen

            print( "".join( currentframe ))  # output currentframe

            time.sleep( framedelay )  # inter-frame delay

main()
