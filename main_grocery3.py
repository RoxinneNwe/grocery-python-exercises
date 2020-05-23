# This is your Main program entry point
# Call from grocery3.py using from <the name of the file grocery3.py> import * where * is a placeholder assigning it
# to ALL content from the grocrey3.py
from grocery3 import grapes, veggie, total_value
x = 13.50  # this will use on grapes function
y = 12.50  # this will use on veggie function

# under function grapes, the correct parameter will be below:
grapes(x)
veggie(y)

print(f"The value of grapes is {grapes(x)}")
print(f"The value of veggie is {veggie(y)}")

grape_input = float(input("Enter grapes value: "))
total_grape_value = grape_input * grapes(x)
print(f"Total value for grapes is: AED {total_grape_value}")

veggie_input = float(input("Enter grapes value: "))
total_veggie_value = veggie_input * veggie(y)
all_total = total_grape_value + total_veggie_value
print(f"Total value for grapes is: AED {total_veggie_value}")
print(f"Sum of all items is: {total_value(all_total)}")
