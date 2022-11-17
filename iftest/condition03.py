#!/usr/bin/env python3

# get user input for hostname
hostname = input("What should we call hostname?")

# use str.lower() to return lower-case string and make sure it matches expected value
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

# always print out to the user
print("Exiting the script.")
