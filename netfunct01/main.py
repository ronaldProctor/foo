#!/usr/bin/env python3
"""Title block."""

import crayons
import json

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {ip}') #fstring
        # we'll learn code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to send command --> {mycmds}')
            # we'll learn code that sends cmds to device here

    return None

# function to reboot device
def devicereboot(devicecmd): # devicecmd == dict
    for i in devicecmd.keys(): #looping through the dict
        print(f'Rebooting IP: {i}')

# start our main script
def main():
    """called at runtime"""

    with open("devicecmd.json", "r") as devicecmdfile:
         devicecmd = json.load(devicecmdfile) # load and decode the json file

    print("Welcome to the network device command pusher") # welcome message

    # get dataset
    print("\nData set found\n") # replace with a function call that reads the dataset

    # run
    commandpush(devicecmd) # call function to push commands to devices
    devicereboot(devicecmd) # try to reboot things

# call our main function
main()
