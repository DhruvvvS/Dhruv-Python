# Problem for practice input function

#  AREA OF RECTANGLE (length * breadth)

l = float(input("Length: "))
b = float(input("Breadth: "))

area = l*b
print(f"Area of rectangle is {area}cm²")
# You can also write above statement like this 
# print(f"Area of rectangle is {l*b}")

# Another problem
# Shopping Cart problem
item = input ("Name the item you want to buy : ")
price = float(input("At what price do you want to buy : "))
quantity = int(input("How many : "))
total = price * quantity
print(f"Your amount to pay is {total}")