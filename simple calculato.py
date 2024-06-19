#1.1. Create a simple calculator in Python.


a = int(input("Enter No1: "))
op = input("Enter Op: ")
b = int(input("Enter No2: "))

if op == '+':
    print("Ans:", a + b)
elif op == '-':
    print("Ans:", a - b)
elif op == '*':
    print("Ans:", a * b)
elif op == '/':
    if b == 0:
        print("Not Defined")
    else:
        print("Ans:", a / b)
else:
    print("Invalid Input")
