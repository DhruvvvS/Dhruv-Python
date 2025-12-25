# creating a DIAMOND PATTERN
"""  *
    ***
   *****
    ***
     *   """

rows = int(input("Enter the no. of rows (odd): "))
symbol = input("Enter the symbol to be printed: ")

# ensuring taken input is odd
if rows % 2 == 0:
    rows = int(input("Enter the no. of rows again this time in odd:"))

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

    # for spaces in upper half of diamond
    # applying floor division rather than normal division to prevent typeerror as normal division gives answer in float even if operands are integer
    for spaces in range(1, (rows - i // 2) + 1):
        print(" ", end="")

    # for symbol printing in upper half of diamaond
    for j in range(1, i + 1):
        print(symbol, end="")

    # for printing in next line
    print()
