#!/usr/bin/env python3
"""Title block
   Looping across a file opened with 'with'"""

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    #file stays open while inside this 'with'
    # create a list of lines
    dnslist = dnsfile.readlines()

    #loop over lines
    for svr in dnslist:
        #print and end w/o newline
        print(svr, end="")

#file automagically closed after exiting 'with'
