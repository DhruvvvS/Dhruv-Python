# HANGMAN GAME 

# importing random and time module
import random
import time

# downloaded nltk module to get library of words containing approx 236000 words
# importing words file from nltk module
from nltk.corpus import words
# making a list of all the words imported from nltk
word_list = list(words.words())

# ASCII art of hangman made in dictionary in which values are tuple
hangman_art = {0:(" +----+" ,
                  " |    |" ,
                  "      |" ,
                  "      |" ,
                  "      |" ,
                  "      |" ,
                  "______|") , 

               1:(" +----+" ,
                  " |    |" ,
                  " O    |" ,
                  "      |" ,
                  "      |" ,
                  "      |" ,
                  "______|") ,

               2:(" +----+" ,
                  " |    |" ,
                  " O    |" ,
                  " |    |" ,
                  "      |" ,
                  "      |" ,
                  "______|") ,

               3:(" +----+" ,
                  " |    |" ,
                  " O    |" ,
                  "/|    |" ,
                  "      |" ,
                  "      |" ,
                  "______|") ,

               4:(" +----+" ,
                  " |    |" ,
                  " O    |" ,
                  "/|\\   |" ,
                  "      |" ,
                  "      |" ,
                  "______|") ,

               5:(" +----+" ,
                  " |    |" ,
                  " O    |" ,
                  "/|\\   |" ,
                  "/     |" ,
                  "      |" ,
                  "______|") ,
                  
               6:(" +----+" ,
                  " |    |" ,
                  " O    |" ,
                  "/|\\   |" ,
                  "/ \\   |" ,
                  "      |" ,
                  "______|") }

# function to display hangman art according to wrong guesses by user
def display_man(wrong_guesses):
   print("**********")
   print()

   # loop to print each line of tuple
   for line in hangman_art[wrong_guesses]:
      print(line)

   print()
   print("**********")
    
# function to display hint 
def display_hint(hint,filtered_word):
    
   # adding gap in between each hint
    print(" ".join(hint))
    print()

   # conditions for length of hint and printing for fun
    if 3 <= len(filtered_word) <= 5:
       print("* * * * *")

    elif 6 <= len(filtered_word) <= 8:
       print("* * * * * * *")

    elif len(filtered_word) >= 9:
       print("* * * * * * * * * * *")

# function to display the answer 
def display_answer(answer):

   # adding gap in between each answer 
    print(" ".join(answer))

# main function
def main():

   # printing start of game
   print("***********************")
   print("WELCOME TO HANGMAN GAME")
   print("***********************")

   # asking for user input to choose difficulty of game
   difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

   # conditions for each difficulty
   if difficulty == "easy":
      filtered_word = [w for w in word_list if 3 <= len(w) <= 5]

   elif difficulty == "medium":
      filtered_word = [w for w in word_list if 6 <= len(w) <= 8]

   elif difficulty == "hard":
      filtered_word = [w for w in word_list if len(w) >= 9]

   # choosing a random word from list made of words and storing it in the answer variable 
   answer = random.choice(filtered_word)
   
   # hint is nothing but blank spaces equal to length of the word
   hint = ["_"] * len(answer)

   # initialising variable for wrong guesses
   wrong_guesses = 0

   # initialising and creating a set to store guessed letter
   guessed_letter = set()

   # making it True for while loop
   is_running = True

   while is_running:

      # calling both functions and showing hint
      display_man(wrong_guesses)   
      display_hint(hint,filtered_word)

      # user input of letter
      guess = input("Enter a letter: ").lower()

      # condition if user input is not a single letter or a digit
      if len(guess) != 1 or not guess.isalpha(): 
         print("Invalid Input. 😐")
         print("Please enter a letter.")
         continue

      # condition if a letter is guessed twice
      if guess in guessed_letter: 
         print(f"You already guessed {guess}.")
         continue

      # adding the input letter in set made of guessed letter
      guessed_letter.add(guess)

      # condition if letter is also in answer 
      # also replacing the _ (blank space) of hint with correct guessed letter
      if guess in answer:
         for i in range(len(answer)):
             if answer[i] == guess:
                 hint[i] = guess

      # incrementing count of wrong guesses     
      else:
          wrong_guesses += 1

      # winning condition as all blank spaces are filled
      # calling functions to display answer and hangman
      if "_" not in hint:
          display_man(wrong_guesses)
          display_answer(answer)
          print("--------------")
          print("   HURRAY 🎉 ")
          print("    WON!! 🥳 ")
          is_running = False
         
      # losing condition as count of wrong guesses passed the length of the dictionary key
      # calling functions to display answer and hangman
      elif wrong_guesses >= len(hangman_art) - 1 :
          display_man(wrong_guesses)
          display_answer(answer)
          print("--------------")
          print("   SORRY 😔   ")
          print("  YOU LOST 🫠 ")
          is_running = False
                   
   print("GAME OVER 💀")
   time.sleep(0.5)
   print("PLAY AGAIN ")

if __name__ == "__main__":
    main()