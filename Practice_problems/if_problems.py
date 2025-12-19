# WEIGHT CONVERTER

weight = float(input("Enter your weight: "))
unit = input("Enter the unit of weight which is in (K or L): ")

if unit == "K":
    weight *= 2.205
    unit = "lbs (pounds)"
    print(f"Your weight in pounds is {round(weight,2)} {unit}.")

elif unit == "L":
    weight /= 2.205
    unit = "kgs (kilograms)"
    print(f"Your weight in kilograms is {round(weight,2)} {unit}.")

else:
    print(f"{unit} is not valid.")



# TEMPERATURE CONVERTOR FOR TWO UNITS

temp = float(input("Enter the temp. "))
unit = input("Enter the unit of temp. (c or f): ")

if unit == "c":
    temp = round(((9 * temp)/5) + 32 , 2)
    print(f"The temp in fahrenhait will be {temp}°F")

# For degree (°) sign --> Alt + 0176

elif unit == "f":
    temp = round(((temp - 32) * 5) / 9 , 2)
    print(f"The temp in degree celsius will be {temp}°C")

else:
    print(f"{unit} is not valid.")


# TEMPERATURE CONVERTOR FOR THREE UNITS

temp = float(input("Enter the temp. "))
unit = input("Enter the unit of temp. (c or f or k): ")
con = input ("Enter the unit to convert temp. in (c or f or k): ")
# For degree (°) sign --> Alt + 0176

if unit == "c":
    if con == "f":
        temp = round(((9 * temp)/5) + 32 , 2)
        print(f"The temp in fahrenhait will be {temp}°F")
    elif con == "k":
        temp += 273.15
        print(f"The temp in kelvin will be {temp}K")

elif unit == "f":
    if con == "c":
        temp = round(((temp - 32) * 5) / 9 , 2)
        print(f"The temp in degree celsius will be {temp}°C")
    elif con == "k":
        temp = round(((temp - 32) * 5) / 9 + 273.15 , 2)
        print(f"The temp in kelvin will be {temp}K")

elif unit == "k":
    if con == "c":
        temp -= 273.15
        print(f"The temp in degree celsius will be {temp}°C")
    elif con == "f":
        temp = round(((temp - 273.15) * 9 / 5) + 32 , 2)
        print(f"The temp in fahrenhait will be {temp}°F")

else:
    print(f"{unit} is not valid.")