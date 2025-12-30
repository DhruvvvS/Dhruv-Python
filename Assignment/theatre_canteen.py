# It is a simple concession stand program (place in theatre from where we buy our snacks)

# creating a dictionary for menu b'coz it will show both items and money
menu = {
    "popcorn": 250.00,
    "fries": 125.00,
    "nachos": 100.00,
    "chips": 75.00,
    "pizza": 350.00,
    "pepsi": 125.00,
    "diet coke": 175.00,
}

# declaring and initialising cart and total as it will be according to user input
cart = []
total = 0

# just for aesthetics
print("------------------------")
print("          MENU          ")
print("------------------------")
print()

print(" Items", "      Rupees")
# this loop would print the whole menu using items function
for key, value in menu.items():
    print(f"{key:10} : {value:.2f}")

print()

# taking input from user
while True:
    food = input("Enter the food item you would like to eat (q to quit): ").lower()
    if food == "q":
        break
    elif (
        menu.get(food) is not None
    ):  # is not None means it contains the food item written by user in the menu dictionary
        cart.append(food)  # adding the user food to the cart tuple

# just for aesthetics
print("------------------------")
print("       YOUR ORDER       ")
print("------------------------")

# this loop will print the food in the cart and incraese the total amount
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print()

# prints the total amount
print(f"Your Total is {total:.2f} Rupees.")
