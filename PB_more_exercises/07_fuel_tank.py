type =input()
fuel = float(input())

FUEL_BOUNDARY = 25
is_valid_fuel = False

if type == 'Diesel' or type == 'Gasoline' or type =='Gas':
    is_valid_fuel = True

if not is_valid_fuel:
    print("Invalid fuel!")
elif fuel >= FUEL_BOUNDARY:
    print(f"You have enough {type.lower()}.")
else:
    print(f"Fill your tank with {type.lower()}!")