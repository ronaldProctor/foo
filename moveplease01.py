#!/usr/bin/env python3

# import things from standard library
import shutil
import os

def main():

    # change to working directory
    os.chdir('/home/student/mycode/')

    # move raynor.obj to storage
    shutil.move('raynor.obj', 'ceph_storage/')

    # Prompt for new name
    xname = input('What is the new name for kerrigan.obj? ')

    # Rename with user input
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()
