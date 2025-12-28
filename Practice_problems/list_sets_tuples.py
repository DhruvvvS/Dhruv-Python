# Creating a small program to learn and try all functions in collections

# LIST :--

# here num is the actual list and num_list is just a temporary variable to append the user input to the actual list

num = []
for i in range(0,5):
    num_input = input("Enter the num to input: ")
    num_list = num.append(num_input)
# append functions to add the element from last

print(num)
print(len(num))
print("5" in num) # find the element in the list
num.insert(2, "9") # this inserts the element at particular index
num.sort() # sorts out the list in numerical or alphabetical order
print(num)
num.reverse() # reverses whole list
print(num)
print(num.count("8")) # counts how many times the particular element came in the list


# SET :--

# here h is the actual set and char_set is just a temporary variable to append the user input to the actual set

char = []
for i in range(0,5):
    char_input = input("Enter the alphabet to input: ")
    char_set = char.append(char_input)
h = set(char)
#  In sets using add or append function shows error so we need to form a list then convert it to set by typecasting


print(h)
print(len(h))
print("b" in h) # find the element in the set
h.add("S") # adds the element at random index
print(h)
h.remove("a") # removes the element
print(h)
h.clear() # clears whole set

# TUPLES :--

# here y is the actual tuple and x_tuple is just a temporary variable to append the user input to the actual tuple

x = []
for i in range(0,5):
    x_input = input("Enter the character to input: ")
    x_tuple = x.append(x_input)

y = tuple(x)
# In tuples we can't use add or append function so we need to form a list then convert it to tuple by typecasting

print(y)
print(len(y))
print("b" in y)
print(y.index("k")) # finds the index no. at which that element is
print(y.count("a")) # counts no. of times element came in that tuple