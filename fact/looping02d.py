#!/usr/bin/env python3
"""Looping across a file with 'with'
   while also being gentle on memory consumption.
   Sort domains ending in .org and .com into files
   org-domain.txt and com-domain.txt"""

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    # loop across lines in the file
    for svr in dnsfile:
        svr = svr.rstrip('\n') # remove newline char

        # if string svr ends in 'org'
        if svr.endswith('org'):
            with open("org-domain.txt", "a") as srvfile: # a to append
                srvfile.write(svr + "\n")

        # else-if the string svr ends with 'com'
        if svr.endswith('com'):
            with open("com-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")

