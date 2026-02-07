# PYTHON ENCRYPTION PROGRAM 

# importing random and string module
import random
import string

# initialising variable 
# string functions to all characters from keyboaed
chars = " " + string.punctuation + string.ascii_letters + string.digits

# casting chars variable in to list to make printing easy
chars = list(chars)

# making a copy of chars list in key variable to create a encrypted and shuffle key list
keys = chars.copy()

# shuffling the element of the keys list
random.shuffle(keys)

# ENCRYPTION 

# user input for msg to encrypt
plain = input("Enter a msg to encrypt: ")

# initialising cipher string variable
cipher = ""

# loop to go to each of the element from the list 
for letter in plain:

    # .index function shows the index of corresponding iteration from chars list and storing it in index variable
    index = chars.index(letter)

    # adding the corresponding element from keys of that index to cipher variable
    cipher += keys[index]

# Results
print("-----------------------")
print(f"Original msg: {plain}")
print(f"Encrypted msg: {cipher}")
print("-----------------------")

# DECRYPTION

# user input for msg to decrypt
cipher = input("Enter a msg to decrypt: ")

# initialising plain string variable
plain = ""

# loop to go to each of the element from the list 
for letter in cipher:
    index = keys.index(letter)
    plain += chars[index]

# Results
print("-----------------------")
print(f"Encrypted msg: {cipher}")
print(f"Original msg: {plain}")
print("-----------------------")