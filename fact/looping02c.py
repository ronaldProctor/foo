#!/usr/bin/env python3
"""Using 'with' to open and loop across text files"""

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    #loop across lines in file
    for svr in dnsfile:
        #print and end w/o newline
        print(svr, end="")

# file is automatically closed
