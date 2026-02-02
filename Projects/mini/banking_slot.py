# PYTHON BANKING PROGRAM 

# function for showing balance
def show_balance():
    print(f"Your account balance is ${balance:.2f}")

# function for deposting money in account
def deposit():
    amount = float(input("Enter the amount to be deposited: "))

    # when amount entered by user is negative
    if amount < 0:
        print("Please enter a valid amount")
        return 0
    
    else:
        return amount

# function for withdrawing money from account
def withdraw():
    amount = float(input("Enter the amount to be withdrawn: "))

    # when amount entered by user is negative 
    if amount < 0:
        print("Please enter a valid amount to withdrawn")
        print("Amount to withdraw should be greater than Zero.")
        return 0
    
    # when amount to withdraw is more than balance in the account
    elif amount > balance:
        print("INSUFFICIENT FUNDS")
        return 0
    
    else:
        return amount 

# initialising variables
balance = 0
is_running = True

# for aesthetics
print("**********************************")
print("          BANKING SLOT            ")
print("**********************************")

# while loop for showing options to user
while is_running:

    print("----------------------------------")   

    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    # taking user input
    choice = input("Enter your choice (1-4): ")

    print("----------------------------------")   

    # match case for different-different choices
    match choice:

        case '1':
            show_balance()
        
        case '2':
            balance += deposit()
        
        case '3':
            balance -= withdraw()
        
        case '4':
            is_running = False
        
        case _ :
            print("Not a valid choice.")

print() 

print(f"Balance in your account : ${balance:.2f}")
print("Have a Wonderful Day!")

print()
print("----------------------------------")   