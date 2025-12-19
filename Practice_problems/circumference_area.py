#### CIRCUMFERENCE OF CIRCLE ####
import math
r = int(input("Radius of the circle : "))

# directly multiplying with constant
c = 2*math.pi*r
print(f"Circumference of circle is {round(c,2)} cm²")

# defining constant in different variable
con = math.pi
c = 2*con*r
print(f"Circumference of circle is {round(c,2)} cm²")

#### AREA OF CIRCLE ####
r = int(input("Radius of the circle : "))

# directly using functions
a = math.pi*pow(r,2)
print(f"Area of circle is {round(a,2)} cm²")

# defining functions differently
p = pow(r,2)
a = con*p
print(f"Area of circle is {round(a,2)} cm²")