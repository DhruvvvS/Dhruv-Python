import random
import time

def spin_row():
    symbols = ["🍒","💎","🔔","🍉","⭐"]
    
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results

def print_row(row):

    print("-----------------")
    print("  |  ".join(row))
    print("-----------------")

def get_payout():
    pass

print("*****************************")
print("    WELCOME TO SLOT GAME     ")
print(" SYMBOLS : 🍒 💎 🔔 🍉 ⭐ ")
print("*****************************")

balance = 10000
time.sleep(0.3)

while balance > 0:

    print(f"Your current balance is ${balance}")

    bet = int(input("Amount you want to bet: "))

    if bet <= 0:
        print("Bet amount should be greater than Zero.")

    if bet > balance:
        print("Insufficient Funds ☹️")
    
    balance -= bet

    row = spin_row()

    time.sleep(0.3)
    print("SPINNING...")
    time.sleep(0.5)

    print_row(row)

    reward = get_payout(row,bet)

    play = input("Do you want to play again (Y/N): ").upper()

    if play != "Y":
        break

print("-----------------------")
print("        RESULTS        ")
print("-----------------------")