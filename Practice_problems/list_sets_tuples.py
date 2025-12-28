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

# here char is the actual set and char_set is just a temporary variable to append the user input to the actual set

char = {}
for i in range(0,5):
    char_input = input("Enter the num to input: ")
    char_set = char.append(char_input)
# append functions to add the element from last

print(char)
print(len(char))
print("b" in char) # find the element in the set
char.add("S") # adds the element at random index
print(char)
char.remove("a") # removes the element
print(char)
char.clear() # clears whole set

# TUPLES :--

# here x is the actual tuple and x_tuple is just a temporary variable to append the user input to the actual set

x = ()
for i in range(0,5):
    x_input = input("Enter the num to input: ")
    x_tuple = x.append(x_input)
# append functions to add the element from last

print(x)
print(len(x))
print("b" in x)
print(x.index("k")) # finds the index no. at which that element is
print(x.count("a")) # counts no. of times element came in that tuple