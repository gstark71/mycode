#!/usr/bin/env python3
"""GSTARK TEST LAB
   print() - NO ZOMBIES YET"""

def main():

    # collect string input from the user
    user_input = input("Where would you hide from zombies:")
    
    ## the line below creates a single string that is passed to print()
    # print("You would hide: " + user_input)
    
    ## print() can be given a series of objects separated by a comma
    print("You would realy want to hide:", user_input)

main()

