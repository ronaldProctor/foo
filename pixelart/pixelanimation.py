#!/usr/bin/env python3

"""terminal output animation experiments"""

#  get smarter
import random
import math
import os
import time

#  x and y dimensions
x = 8
y = 8

#  delay between frames (s)
f = 0.2 

def randogrid( x, y ):                      #  generates a randomized grid of dots

    for i in range(y):                      #  y dimension (rows)
        for j in range(x):                  #  x dimension (columns)
            k = random.random()             #  k = random float
            if k <= 0.5: 
                print("\u25c9 ", end = "")  #  unicode closed dot
            else:
                print("\u25ef ", end = "")  #  unicode open dot
        print("")                           #  next line for next row

while True:               #  do this stuff a lot
    os.system("clear")
    randogrid(x,y)
    time.sleep(f)
