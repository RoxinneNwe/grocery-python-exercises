# Exercise 1:

# On this exercise, we are implementing a code for a grocery receipt
# Declared constant variables

grapes = 13.50
vegtable = 12.50
vat = .05  # this is 5% total of items

print("====================")
print("Ansari Grocery Store:")
print("=====================")

total_grapes = 3 * grapes
total_vegies = 2 * vegtable
total_sum = total_grapes + total_vegies
with_vat = total_sum * vat
final_payment = with_vat + total_sum

# pseduo code
# Customer buys
# 3 qty of grapes = xxx
# 2 qty of vegies = xxx
# Total purchase included VAT(5%) = xxx

print(f"3 qty of grapes = {total_grapes}")

print(f"2 qty of veggies = {total_vegies}")
print(f"Total payment with VAT(5%) = {final_payment}")
print("=====================")
print("Have a nice day!")
