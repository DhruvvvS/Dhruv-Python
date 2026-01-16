#  NUMBER GUESSING GAME
#  user has to guess the number which is been random selected
#  importing random module to get random number to guess for the game
#  importing time module to get some fun by making use of time sleep function
 
import random
import time

# Initialising variables 
# guesses to increase every time user gets the guess wrong
a = 1
b = 100
guesses = 0

# randint function to select a random integer
guessed_no = random.randint(a,b)

# Taking user input
guess = int(input("Enter your guess: "))

# Initialising while loop
while True:
    # condition if user guesses number out of bound
    if guess < 0 or guess > 100:
        print("Number out of bound")
        guess = int(input("Enter your guess again this time in bound: "))

    elif guess < guessed_no:
        print("TOO COLD")
        guess = int(input("Enter your guess again: "))
        guesses += 1

    elif guess > guessed_no:
        print("TOO HOT")
        guess = int(input("Enter your guess again: "))
        guesses += 1

    # condition when guess = guessed_no
    else:
        print("-----------------------------------------")
        print("                HURRAY!!!                ")
        print("          YOU GUESSED IT RIGHT!          ")
        print("-----------------------------------------")
        break

# applying time sleep function to make it more fun
time.sleep(1)

# if condition because what if the user guesses the number in his first try
if guesses == 0: 
    # Printing Results
    print("                RESULTS              ")
    print("               HURRAY!!!             ")
    print("     You guessed it in First chance.  ")

# else print this result
else:
    # Printing Results
    print("                RESULTS                 ")

    # adding one(1) in final number of guesses to include the guess for final answer also
    print(f"    You required {guesses+1} number of guesses.")

    print("               TRY AGAIN                 ")
    print("This time try to guess in less guesses :)")