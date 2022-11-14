#!/usr/bin//env python3
"""
Alta3 Research | RZFeeser
print() - concatenate vs print a series of items
"""

def main():

    #Collect user input
    user_input = input("Please enter an IPv4 IP address:")
    user_vendor = input("Vendor Name:")
    ## The line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input)


    ## print() can be given a series of objects separated by a comma
    print("You told me the IPv4 address is:", user_input)
    print("Vendor Name:", user_vendor)



main()
