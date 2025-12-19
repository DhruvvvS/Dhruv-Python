# PYTHON CALCULATOR 

a = int(input("Enter first number : "))
operator = input("Enter operation : ")
b = int(input("Enter second number : "))

if operator == "+":
    c = a + b
    print(f"The answer is {c}")
elif operator == "-":
    c = a - b
    print(f"The answer is {c}")
elif operator == "*":
    c = a * b
    print(f"The answer is {c}")
elif operator == "/":
    c = a / b
    print(f"The answer is {c}")
else:
    print(f"{operator} is not a valid operator")