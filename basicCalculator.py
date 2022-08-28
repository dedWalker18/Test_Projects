# import math

print("Basic Calculator")

x, op, y = input("Enter the Calculation: ").split()                                                                     #Takinng Input of Operation

x = int(x)
y = int(y)

if op == "+":                                                                                                           # Main Body
    print(x, op, y, "=", x + y)
if op == "-":
    print(x, op, y, "=", x - y)
if op == "*":
    print(x, op, y, "=", x * y)
if op == "/":
    print(x, op, y, "=", x / y)

# END