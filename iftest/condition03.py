#!/usr/bin/env python3
hostname = input("What value should we set for hostname?")

## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("The hostname matches the expected config")

# Always print out to the user
print("exiting the script")
