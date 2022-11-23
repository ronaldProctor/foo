#!/usr/bin/env python3

"""
    alphabet_v1.py November 2022
    R. Proctor | ron@proctorcreative.com

    Looks up and returns ASCII art "fonts" from text files.
"""

# list of allowed letters
whitelist = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# open the file with the ascii art
with open("3dfont.txt", "r") as fonts:

    # read-in the lines
    linelist = fonts.readlines()
    #print("linelist =", linelist) #--debug

    # get user input
    letter = input("Please enter a single letter A-Z: ")
    #print("letter =", letter) #--debug

    # take only the first letter from user imput
    target = letter[0]
    #print("target =", target) #--debug

    #convert target to upper case
    target = target.upper()
    #print("target =", target) #--debug

    # check target against whitelist
    if target in whitelist:
        
        # if found in whitelist
        #print(target, " is in whitelist.") #--debug
        
        # get index of target in linelist
        i = linelist.index( target + "\n" )
        # print("i =", i) #--debug

        # get the lines i+1:i+7
        artlines = linelist[ i+1 : i+8 ]
        #print(artlines) #--debug

        # output
        print("".join(artlines))

    else:
        # message if not found in list
        print(target, " is not in the whitelist.")

