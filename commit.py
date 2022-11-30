#!/usr/bin/env
"""Proctor Creative LLC | ron@proctorcreative.com
    Automagic git commit and push."""

# get smarter
import os

print("\nCommitting to repository ...\n")

comment = input("Please enter your commit comment: ")  # get user comment for commit

if comment == "":
    comment = "No comment."

print("Command: cd ~/mycode")
os.system("cd ~/mycode")

print("Command: pwd")
os.system("pwd")

print("Command: git add *")
os.system("git add *")

commandstring = "git commit -m \"" + comment + "\""
print("Command:", commandstring)
os.system(commandstring)

print("Command: git push origin HEAD")
os.system("git push origin HEAD")


