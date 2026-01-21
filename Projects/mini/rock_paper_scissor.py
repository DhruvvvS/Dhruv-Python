# ROCK PAPER SCISSORS GAME

# importing random module to create a random choice from rock, paper and scissors
import random

# importing time module
import time

# creating a tuple for choices 
a = ("Rock","Paper","Scissors")

# initialising variables
score = 0
plays = 0

# while loop to play as many times I want
while True:

    # taking input from user
    user = input("Rock, Paper, Scissors (q to quit the game): ").capitalize()
    
    # condition to quit the game
    if user == "Q":
        break
    
    # condition if input made by user is not in the tuple "a"
    while user not in a:
        print("You have to make choice between (Rock, Paper, Scissors).")
        user = input("Rock, Paper, Scissors (q to quit the game): ").capitalize()

    # for fun and making it more like the actual game
    print("ROCK")
    time.sleep(0.3)

    print("PAPER")
    time.sleep(0.3)

    print("SCISSORS")
    time.sleep(0.3)

    # choosing random using choice function from the list 'a' (Rock, Paper, Scissors)
    b = random.choice(a)

    # printing what computer played
    print(f"Computer Played {b}.")

    # condition if user and computer played same.
    if b == user:
        print("Draw")
        print("Play again.")
        
    # condition if the choice made by computer is Rock and in it nested ifs as if user chose different inputs.
    elif b == "Rock":

        if user == "Scissors":
            print("You Lose :( ")
    
        elif user == "Paper":
            print("You Win :) ")
            score += 1

    # condition if the choice made by computer is Paper and in it nested ifs as if user chose different inputs.
    elif b == "Paper":

        if user == "Rock":
            print("You Lose :( ")
    
        elif user == "Scissors":
            print("You Win :) ")
            score += 1

    # condition if the choice made by computer is Scissors and in it nested ifs as if user chose different inputs.
    elif b == "Scissors":

        if user == "Paper":
            print("You Lose :( ")
    
        elif user == "Rock":
            print("You Win :) ")
            score += 1

    print("----------------------------")

    # increasing play count as we completed one iteration
    plays += 1

time.sleep(0.3)
# printing results
print("----------------------------")
print("          RESULTS           ")
print("----------------------------")

# printing how many times user played and how many time he won the games against computer
print(f"You played {plays} time.")
print(f"And won {score} time.")

# just for fun
print("----------------------------")
print("         TRY AGAIN          ")
print("        AND WIN MORE        ")