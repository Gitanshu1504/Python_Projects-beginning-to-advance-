balance = 10000.0

while True:
  print("\n--- ATM Menu ---")
  print("1. Check Balance")
  print("2. Deposit")
  print("3. Withdraw")
  print("4. Exit Program")

  choice = input("Enter your choice (1-4): ")

  if choice == "1":
    print(f"Your current balance is: ₹{balance}")

  elif choice == "2":
    amount = float(input("Enter deposit amount: "))
    if amount > 0:
      balance += amount
      print(f"₹{amount} deposited successfully.")
      print(f"Updated balance: ₹{balance}")
    else:
      print("Invalid deposit amount.")

  elif choice == "3":
    amount = float(input("Enter withdrawal amount: "))
    if 0 < amount <= balance:
      balance -= amount
      print(f"₹{amount} withdrawn successfully.")
      print(f"Updated balance: ₹{balance}")
    elif amount > balance:
      print("Insufficient balance!")
    else:
      print("Invalid withdrawal amount.")

  elif choice == "4":
    print("Thank you for using the ATM. Goodbye!")
    break

  else:
    print("Invalid choice! Please enter a number between 1 and 4.")
