#!/usr/bin/env python3

# get smarter
import subprocess

subprocess.call(["ip", "link", "show", "up"])

print("This program will check your interfaces.")

interface = input("Enter an interface (ex: ens3):")

subprocess.call(["ip", "addr", "show", "dev", interface])

subprocess.call(["ip", "route", "show", "dev", interface])
