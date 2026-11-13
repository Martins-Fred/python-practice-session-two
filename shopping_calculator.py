price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
money = float(input("How much money do you have? "))

total = price * quantity

print("Total cost:", total)
print("Money remaining:", money - total)
print("Do you have enough money?", money >= total)
