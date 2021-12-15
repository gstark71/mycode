#!/usr/bin/env python3
"""Stark Labs | Gstark
   Using a files lines as a source for the for-loop"""

# open file in read
dnsfile = open("dnsservers.txt", "r")

# create list of lines
dnslist = dnsfile.readlines()

# loop over lines 
for svr in dnslist:
    #print and end new line
    print(svr, end="")

# close file 
dnsfile.close()
