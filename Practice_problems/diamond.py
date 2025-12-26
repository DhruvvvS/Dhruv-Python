# creating a DIAMOND PATTERN
"""  *
    ***
   *****
    ***
     *   """

rows = int(input("Enter the no. of rows (odd): "))

# ensuring taken input is odd
while rows % 2 == 0:
    print("Rows are even, please type in odd number for rows.")
    rows = int(input("Enter the no. of rows again this time in odd:"))

symbol = input("Enter the symbol to be printed: ")

# for upper half of diamond
for i in range(1, rows + 1, 2):

    # for spaces in upper half of diamond
    # applying floor division rather than normal division to prevent typeerror as normal division gives answer in float even if operands are integer
    for spaces in range(1, (rows - i // 2) + 1):
        print(" ", end="")

    # for symbol printing in upper half of diamaond
    for j in range(1, i + 1):
        print(symbol, end="")

    # for printing in next line
    print()


# for lower half of diamond
for i in range(rows - 2, 0, -2):

    # for spaces in lower half of diamond
    # applying floor division rather than normal division to prevent typeerror as normal division gives answer in float even if operands are integer
    for spaces in range(1, (rows - i // 2) + 1):
        print(" ", end="")

    # for symbol printing in lower half of diamaond
    for j in range(1, i + 1):
        print(symbol, end="")

    # for printing in next line
    print()


# creating a DIAMOND PATTERN in Numbers
"""     1
       123
      12345
       123
        1   """

rows = int(input("Enter the no. of rows (odd): "))

# ensuring taken input is odd
while rows % 2 == 0:
    print("Rows are even, please type in odd number for rows.")
    rows = int(input("Enter the no. of rows again this time in odd:"))


# for upper half of diamond
for i in range(1, (rows // 2) + 1):

    # for spaces in upper half of diamond
    # applying floor division rather than normal division to prevent typeerror as normal division gives answer in float even if operands are integer
    for spaces in range(1, (rows - i ) + 1):
        print(" ", end="")

    # for symbol printing in upper half of diamaond
    for j in range(1, (2 * i - 1) + 1):
        print(j, end="")

    # for printing in next line
    print()


# for lower half of diamond
for i in range((rows // 2) + 1, 0 , -1):

    # for spaces in lower half of diamond
    # applying floor division rather than normal division to prevent typeerror as normal division gives answer in float even if operands are integer
    for spaces in range(1, (rows - i ) + 1):
        print(" ", end="")

    # for number printing in lower half of diamaond
    for j in range(1, (2 * i - 1) + 1):
        print(j, end="")

    # for printing in next line
    print()


# creating a DIAMOND PATTERN in Numbers
"""   A
     BCD
    EFGHI
     JKL
      M  """

rows = int(input("Enter the no. of rows (odd): "))

# ensuring taken input is odd
while rows % 2 == 0:
    print("Rows are even, please type in odd number for rows.")
    rows = int(input("Enter the no. of rows again this time in odd:"))

# ord function for ASCII value
value = ord("A")

# for upper half of diamond
for i in range(1, (rows // 2) + 1):

    # for spaces in upper half of diamond
    # applying floor division rather than normal division to prevent typeerror as normal division gives answer in float even if operands are integer
    for spaces in range(1, (rows - i ) + 1):
        print(" ", end="")

    # for symbol printing in upper half of diamaond
    for j in range(1, (2 * i - 1) + 1):
        print(chr(value), end="")
        value += 1

    # for printing in next line
    print()


# for lower half of diamond
for i in range((rows // 2) + 1, 0, -1):

    # for spaces in lower half of diamond
    # applying floor division rather than normal division to prevent typeerror as normal division gives answer in float even if operands are integer
    for spaces in range(1, (rows - i ) + 1):
        print(" ", end="")

    # for number printing in lower half of diamaond
    for j in range(1, (2 * i - 1) + 1):
        print(chr(value), end="")
        value += 1

    # for printing in next line
    print()