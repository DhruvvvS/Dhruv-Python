# Creating a fun game of question and answer with guess counts

# making tuple collection for questions and answers
# As it doesn't require any changes afterwards, tuples will be ordered and faster than Lists

questions = (
    "Which country has the most time zones in the world?",
    "What was the name of the first ever animal sent to space?",
    "What is the only continent on Earth with no active volcanoes?",
    "Technically, what is the most stolen food item in the world?",
    "What is the only planet in our solar system that rotates clockwise on its axis?",
)

# 2D tuple in tuple collection for organising options as there will be 4 options in each tuple
options = (
    ("A. USA", "B. France", "C. Russia", "D. Phillipines"),
    ("A. Ham", "B. Ape", "C. Martine", "D. Laika"),
    ("A. Asia", "B. Europe", "C. Australia", "D. Africa"),
    ("A. Butter", "B. Cheese", "C. Doughnut", "D. Croissant"),
    ("A. Venus", "B. Earth", "C. Jupiter", "D. Uranus"),
)

# answers are also in tuple as it will not change in mid
answers = ("B", "D", "C", "B", "A")

# creating guesses in list to apply append operation and add guess from each question
guesses = []

# declaring and initialising variables
score = 0
question_num = 0

# loop to iterate each question
for question in questions:
    print("-------------------------")
    print(question)

    # loop to iterate each option rows according to question number
    for option in options[question_num]:
        print(option)

    # taking input from user as answer and converting it in upper case
    guess = input("Enter your answer (A,B,C,D): ").upper()
    # appending taken input as guess in guesses list
    guesses.append(guess)

    # if else statement for correct and incorrect answer
    if guess == answers[question_num]:
        print("CORRECT ANSWER! ;)")
        print("HURRAY!!!!!!!!!")
        score += 1
    else:
        print("OOPS!!")
        print("You guessed it WRONG, INCORRECT ANSWER :( ")
        print(f"The correct answer for this is {answers[question_num].upper()}")

    question_num += 1

# just for aesthetics
print("-------------------")
print("      RESULTS      ")
print("-------------------")

# printing the answers of the questions in an order
print("ANSWERS: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

# printing the guesses from user of the questions in an order
print("YOUR GUESSES: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

# printing how many questions user got correct
print(f"You got {score} questions right.")

# converting the score got into percentage and printing it
score = int((score / len(questions)) * 100)
print(f"Your score is {score}%")

# showing result in a good way
print("--------------------")
if score == 100:
    print("    WELL PLAYED!!    ")
    print("You got it all correct")

else:
    print("Sorry, you messed up at some questions.")
    print("      TRY AGAIN      ")

print("----------------------")
