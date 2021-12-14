#!/usr/bin/env python3
"""SNOW-KING  | STARK
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'This is my reccomendation based on the outside temp: '

# wrap connection in a float() to accept decimals as numbers
connection = float(input("What is the temperature outside use cel as a base?"))

# if input value was higher or equal to -10
if connection >= 10:
    message = message + 'are you kidding it is not cold why are you even using this script!'
elif connection >= 0:
    message = message + 'its cooling off, wear a warm jacket.'
elif connection >= -10:
    message = message + 'your fine, put a jacket gloves and a hat on.'
elif connection >= -15:
    message = message + 'getting cooler dont forget warm socks and scarf, hat and gloves.'
elif connection >= -20:
    message = message + 'getting damn cold put on extra layers and a face covering.'
elif connection >= -30:
    message = message + 'now we are just getting crazy, bundle up with layers, face covering, thick gloves and a warm hat.'
else:
    message = message + 'if it is below -40 just stay in pour a hot drink and try to keep the house warm.'
print(message)
