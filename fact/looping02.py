#/usr/bin/env python3
"""Title block
   Using a file's lines as a source for the for-loop"""

# open file in read mode
dnsfile = open("dnsservers.txt", "r")

# create a list of lines
dnslist = dnsfile.readlines()

# loop over lines
for svr in dnslist:
    # print and end without a newline
    print(":) ", svr, end="") # the lines in the txt already have \n newlines

# close the file because we're done with it
dnsfile.close() # it is best practice to close your files
