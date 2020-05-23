# Exercise #2
# using input() function

grapes = 13.50
veggie = 12.50
vat = .05
print("================================")
print("Welcome to Ansari Grocery Store:")
print("================================")

# Customer will enter the quantity value according to item:
x = float(input("Enter number of quantities grapes: "))
y = float(input("Enter quantity of veggies: "))
total_value_grapes = x * grapes

# Compare the f - (format the string) placeholder
#print(f"{x} grapes you enter.")
#print(f"Total Value is: AED {total_value_grapes}")


total_value_veggies = y * veggie

# print veggies total
#print(f"{y} veggies you enter.")
#print(f"Total Value is: AED {total_value_veggies}")
print("================================")
# Total values
total_sum = total_value_grapes + total_value_veggies
with_vat = total_sum * vat
final_payment = with_vat + total_sum

print(f"{x} qty of grapes = {total_value_grapes}")
print(f"{y} qty of veggies = {total_value_veggies}")
print("================================")
print(f"Total payment with VAT(5%) = AED {final_payment}")
print("================================")
print("Have a nice day!")
