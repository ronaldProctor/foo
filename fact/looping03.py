#!/usr/bin/env python3
"""looping across range() to generate n UUIDs"""

#standard library import to make UUIDs
import uuid

howmany = int(input("How many UUIDs should be generated? "))

print("Generating UUIDs...")

# range is required because an int can not be looped
for rando in range(howmany):
    print( uuid.uuid4() ) # Make a UUID for each time through the loop


