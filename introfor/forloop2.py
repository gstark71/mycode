#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   nesting an if-statement inside of a for loop"""

# create a list of strings
vendors = ["polaris", "arctic cat", "ski-doo", "honda", "can-am", "chinese"]
# create a second list of strings
aproved_vendors = ["honda", "can-am", "arctic cat"]

# loop across the list called vendors
for z in vendors:
    print("\nThe vendor is " + z, end="")
    if z not in aproved_vendors:
        print("-NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended.")


