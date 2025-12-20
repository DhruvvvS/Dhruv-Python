# PYTHON COMPOUND INTEREST CALCULATOR

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principal value: "))
    if principal <= 0:
        print("Principal amount can not be zero.")

while rate <= 0:
    rate = float(input("Enter the Interest rate per annum: "))
    if rate <= 0:
        print("Interest rate can not be zero.")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time can not be zero.")

total = float(principal * pow((1 + rate / 100) , time))

print(f"Your total amount after {time} years of compounding is {total:.2f}")



# using only True in while loop
# BREAK STATEMENT (break) : breaks us and takes us out of the loop
# Here True statement in while loop makes sure that even if principal, time, rate are not zero loops will run

while True:
    principal = float(input("Enter the principal value: "))
    if principal <= 0:
        print("Principal amount can not be zero.")
    else:
        break

while True:
    rate = float(input("Enter the Interest rate per annum: "))
    if rate <= 0:
        print("Interest rate can not be zero.")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time can not be zero.")
    else:
        break

total = float(principal * pow((1 + rate / 100) , time))

print(f"Your total amount after {time} years of compounding is {total:.2f}")