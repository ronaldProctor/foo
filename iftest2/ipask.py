#!/usr/bin/env python3
"""R.Proctor"""

# a string variable
ipchk = input("Apply an IP address: ")

# test to see if string is a string
if ipchk == "192.168.70.1":
    print("Looks like the IP address of the gateway was set: " + ipchk + "This is not recommended.")

elif ipchk:
    print("Looks like the IP address was set: " + ipchk)

else:
    print("No input provided.")

