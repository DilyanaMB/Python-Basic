import math

days = int(input())
food_left_kg = float(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_kg = float(input())

needed_food_kg = days * dog_food_kg + days * cat_food_kg + ((days * turtle_food_kg) / 1000)

if food_left_kg >= needed_food_kg:
    food_leftover = food_left_kg - needed_food_kg
    print(f"{math.floor(food_leftover)} kilos of food left.")
else:
    needed_food_more = needed_food_kg - food_left_kg
    print(f"{math.ceil(needed_food_more)} more kilos of food are needed.")