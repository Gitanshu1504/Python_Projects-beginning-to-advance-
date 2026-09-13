Product_Name = input("Enter the product name:")
Price = int(input("Enter the price:"))
Quantity = int(input("Enter the Quantity:"))


Total = Price * Quantity

if Total >= 5000:
                Discount = Total * 0.2
elif Total >= 3000:
                Discount = Total * 0.15
elif Total >= 1000:
                Discount = Total * 0.1
else:
    Discount = 0


Final_Amount = Total - Discount


print("--------------------------Bill-------------------------------")

print("Produca Name:",Product_Name)
print("Price:",Price)
print("Quantity:",Quantity)
print("Total:",Total)
print("Discount:",Discount)
print("Final Amount:",Final_Amount)

print("------------------------------------------------------------")
