# FLOYD TRIANGLE FOR SYMBOL
""" *
    **
    ***
    **** """

rows = int(input("Enter no. of rows: "))
symbol = input("Enter the symbol to print: ")
# writing rows+1 in range because end range is exclusive in nature

for i in range(1, rows + 1):

    for j in range(1, i + 1):
        print(symbol, end="")
        # end function to make symbol come in one line

    print()
    # ending with blank print function to take the outer loop in next line


# FLOYD TRIANGLE FOR NUMBERS
""" 1
    23
    456
    78910  """

rows = int(input("Enter no. of rows: "))
number = 1
# writing rows+1 in range because end range is exclusive in nature
for i in range(1, rows + 1):

    for j in range(1, i + 1):
        print(number, end="")
        number += 1
        # end function to make numbers come in one line

    print()
    # ending with blank print function to take the outer loop in next line


# FLOYD TRIANGLE FOR ALPHABETS
""" A
    BC
    DEF
    GHIJ  """

rows = int(input("Enter no. of rows: "))
value = ord("A")
# ord() function converts character into their ASCII value

# writing rows+1 in range because end range is exclusive in nature
for i in range(1, rows + 1):

    for j in range(1, i + 1):
        print(chr(value), end="")
        # chr() function converts ASCII value into its corresponding character
        value += 1
        # increasing ASCII value by 1
        # end function to make alphabets come in one line

    print()
    # ending with blank print function to take the outer loop in next line

# INVERTED FLOYD WITH SYMBOLS
""" ****
    ***
    **
    *  """

rows = int(input("Enter no. of rows: "))
symbol = input("Enter the symbol to print: ")
# writing rows+1 in range because end range is exclusive in nature

for i in range(1, rows + 1):
    # adding 1 two times b'coz one is for exclusive nature of range and other is for increasing by 1

    for j in range(1, rows + 1 + 1 - i):
        print(symbol, end="")
        # end function to make asterik come in one line

    print()
    # ending with blank print function to take the outer loop in next line

# FLOYD TRIANGLE ON OTHER SIDE
"""    *
      **
     ***
    **** """

rows = int(input("Enter no. of rows: "))
symbol = input("Enter the symbol to be printed: ")
# writing rows+1 in range because end range is exclusive in nature
for i in range(1, rows + 1):

    for j in range(1, rows + 2 - i):
        print(" ", end="")
        # end function to make space come in one line

    for k in range(1, i + 1):
        print(symbol, end="")

    print()
# ending with blank print function to take the outer loop in next line

# INVERTD FLOYD TRIANGLE ON OTHER SIDE
""" ****
     ***
      **
       * """

rows = int(input("Enter no. of rows: "))
symbol = input("Enter the symbol to be printed: ")
# writing rows+1 in range because end range is exclusive in nature
for i in range(1, rows + 1):

    for j in range(1, i + 1):
        print(" ", end="")
        # end function to make space come in one line

    for k in range(1, rows + 2 - i):
        print(symbol, end="")

    print()
    # ending with blank print function to take the outer loop in next line
