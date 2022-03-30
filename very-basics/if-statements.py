temperature = 35

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print(
        "It's a nice day")  # (20, 30]
elif temperature > 10:
    print("It's a bit cold ") # (10, 20]
else:
    print("It's cold")
print("Done")






weight = float(input("Weight: "))
unit = input("K(g), or L(bs): ")
if unit.upper() == "K":
    converted = str(round(weight / 0.45, 1))
    print("Weight in pounds: " , converted)
elif unit.upper() == "L":
    converted = str(round(weight * 0.45, 1))
    print("Weight in kilograms: " , converted)
else:
    print("Invalid input")




