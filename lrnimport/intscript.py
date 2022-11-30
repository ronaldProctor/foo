#!/usr/bin/env python3

# get smarter
from subprocess import call

# call it
call(["ip", "link", "show", "up"])

print("This program will check your interfaces.")

# what interface to look at?
interface = input("Enter an interface (ex: ens3): ")

# ip addr show dev
call(["ip", "addr", "show", "dev", interface])

# ip route ...
call(["ip", "route", "show", "dev", interface])


