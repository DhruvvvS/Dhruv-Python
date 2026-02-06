# Python SLOT MACHINE GAME
# importing random and time module

import random
import time


# function for spinning the slot
def spin_row():
    # creating a list of symbols so it can be appended to list of result
    # for emojis :- WIN + ;
    symbols = ["🍒", "💎", "🔔", "🍉", "⭐"]

    # for loop for choosing any three symbol out of five and appending them in results.
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results


# function for printing the spinned slot to user
def print_row(row):

    # join function is to add "|" between every symbol
    print("-----------------")
    print("  |  ".join(row))
    print("-----------------")


# function for winning payout scheme for user
def get_payout(row, bet):

    if row[0] == row[1] == row[2]:

        if row[0] == "🍒":
            return bet * 3

        elif row[0] == "🍉":
            return bet * 5

        elif row[0] == "🔔":
            return bet * 10

        elif row[0] == "⭐":
            return bet * 15

        elif row[0] == "💎":
            return bet * 20

    return 0


# creating main function
def main():

    # printing for entering game
    print("*****************************")
    print("    WELCOME TO SLOT GAME     ")
    print(" SYMBOLS : 🍒 💎 🔔 🍉 ⭐ ")
    print("*****************************")

    # initialising variable and giving user some amount to play
    balance = 10000
    time.sleep(0.3)

    # while loop only when user have balance
    while balance > 0:

        print(f"Your current balance is ${balance}")

        # user input for bet to make
        bet = int(input("Amount you want to bet: "))

        # conditions when bet made is either negative or greater than balance
        if bet <= 0:
            print("Bet amount should be greater than Zero.")

        if bet > balance:
            print("Insufficient Funds ☹️")

        # decreasing the bet from balance
        balance -= bet

        # calling spin function and storing it in new variable
        row = spin_row()

        # for fun
        time.sleep(0.3)
        print("SPINNING...")
        time.sleep(0.5)

        # calling print row function to display the spinned slot
        print_row(row)

        # calling the payout function to check if user won or not and storing it in new variable
        reward = get_payout(row, bet)

        # condition if user made any payout money
        if reward > 0:
            print(f"You WON ${reward} 😊")

        else:
            print("Sorry, You lost this Round 😔")

        # adding earned reward money to balance
        balance += reward

        print("-------------------------------")

        # asking user if want to play again
        play = input("Do you want to play again (Y/N): ").upper()

        # condition to get out of while loop
        if play != "Y":
            break

    # for fun
    print("-----------------------")
    print("        RESULTS        ")
    print("-----------------------")

    # printing overall money made
    print(f"You Won overall ${reward}. ")

    print()

    print("COME AGAIN TO TRY OUT YOUR LUCK :)")

    print()
    print("**********************************")


# condition to make only run this code when running when you have the file and not when importing
# this makes code reusability easy
if __name__ == "__main__":
    main()
