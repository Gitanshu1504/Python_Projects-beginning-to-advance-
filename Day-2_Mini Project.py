
a = (input("Enter the Name:"))
b = int(input("Enter The Roll Number:"))

c = int(input("Enter The 1st Subject Marks:"))
d = int(input("Enter The 2nd Subject Marks:"))
e = int(input("Enter The 3rd Subject Marks:"))
f = int(input("Enter The 4th Subject Marks:"))
g = int(input("Enter The 5th Subject Marks:"))

Total = c+d+e+f+g
print("Total is:",Total)

Percentage = (Total/500)*100
print("Percetage is:",Percentage)

# Grade

if(Percentage>=90):
                print("A+")
elif(Percentage<=80):
                print("A")
elif(Percentage<=70):
                 print("B+")
elif(Percentage<=60):
                 print("C")
else:
    print("F")

# Pass/Fail

if(Percentage>=50):
                 print("Pass")
else:
    Print("Fail")
