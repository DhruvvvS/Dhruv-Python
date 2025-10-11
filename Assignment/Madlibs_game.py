# MADLIBS GAME 
# It is a game where you create a story by filling in some words at random and have a funny story
# It is a small input and print function assignment

# Taking the user input for all the words
adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun(person,place,thing): ")
noun2 = input("Enter a noun(person,place,thing): ")
emotion1 = input("Enter an emotion(description): ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter a verb ending with 'ing': ")
emotion2 = input("Enter an emotion(description): ")

# Writing a short story to fit in those inputs taken from user
print(f"Today I went to a {adjective1} park.")
print(f"I was scared when I saw {noun1}")
print(f"{noun1} was eating {noun2}")
print(f"I exclaimed! and felt {emotion1}")
print(f"I decided to {verb1} and {verb2} behind {noun1}")
print(f"But suddenly alarm rang and I {emotion2}")
print(f"It was just a DREAM ;) ")

## This builds up a core foundation in taking user input and printing them using f string