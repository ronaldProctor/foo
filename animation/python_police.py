#!/usr/bin/env/python3

import crayons
import time

x = "FOO"

def animate():

    print("\n")

    for i in range(100):
        print( "\r ", crayons.black("     "), crayons.red("  OO ", bold=True), crayons.white("| PYTHON POLICE |", bold=True), crayons.blue("[BA ]", bold=True), i, end="" )
        time.sleep(0.1)
        print( "\r ", crayons.black("     "), crayons.red("[  O]", bold=True), crayons.white("| PYTHON POLICE |", bold=True), crayons.blue(" B   ", bold=True), i, end="" )
        time.sleep(0.1)
        print( "\r ", crayons.black("     "), crayons.red("     ", bold=True), crayons.white("| PYTHON POLICE |", bold=True), crayons.blue("[   ]", bold=True), i, end="" )
        time.sleep(0.1)
        print( "\r ", crayons.black("     "), crayons.red("[F  ]", bold=True), crayons.white("| PYTHON POLICE |", bold=True), crayons.blue("[  R]", bold=True), i, end="" )
        time.sleep(0.1)
        print( "\r ", crayons.black("     "), crayons.red("[FO ]", bold=True), crayons.white("| PYTHON POLICE |", bold=True), crayons.blue("  AR ", bold=True), i, end="" )
        time.sleep(0.1)
        print( "\r ", crayons.black("     "), crayons.red("[FOO]", bold=True), crayons.white("| PYTHON POLICE |", bold=True), crayons.blue("[BAR]", bold=True), i, end="" )
        time.sleep(0.1)

animate()
print("\n")
print("\n")

