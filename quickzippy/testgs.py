#!/usr/bin/python3
"""Stark Labs | GStark
   a solution to custmoization 01"""

import zipfile
def main():
    """runtime code"""
    
    iszip = input("What files would you like to examine (enter full or relative path)? ")

    if zipfile.is_zipfile(iszip): # returns true if the file is a zip file
        print("Yes! That is a 'zip' file.")
        
    else:
        print("Negative, That is not a 'zip' file.")


if __name__ == "__main__":
    main()
