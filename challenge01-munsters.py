#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Review of Lists and Dictionaries"""

# define a short data set (in real world, we want to read this from a file or API)
munsters = {'endDate': 1966, 'startDate': 1964,\
        'names':['Lily', 'Herman', 'Grandpa', 'Eddie', 'Marilyn']}   # {} creates dict



# Your solution goes below this line
# ----------------------------------


# print the the end dat
print(munsters.get("endDate")) 
                        
# print the start date

print("The Munsters began airing on:", munsters.get("startDate"))

# print all names from the 3rd key 
print("Characters on the Munsters include:", munsters.get("names"))

# Break down the data with a "loop"
names = ['Eddie', 'Lily', 'Grandpa', 'Herman', 'Marilyn']

# create a simple for loop
for x in names:   
    print(x, "is a character on the Munsters")
    # print("---")

# we don't have to use a simple list to loop
print("\nDisplays the same data, but by accessing the nested list within our dict\n")
for x in munsters.get("names"):
    print(x, "is a character on the Munsters")
    
# Add to the munsters
munsters["episodes"] = 70
print(munsters)

