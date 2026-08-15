guess = int(input("Enter the guess number:"))

number = 7

if(number<guess):
    print("Too low")

elif(number>guess):
    print("Too High")
else:
    print("Correct!")
    break