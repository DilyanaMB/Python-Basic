degrees = int(input())
time = input()
outfit = ''

if time.lower() == 'morning':
    if 10 <= degrees <= 18:
        outfit = 'Sweatshirt and Sneakers'
    elif 18 < degrees <= 24:
        outfit = 'Shirt and Moccasins'
    else:
        outfit = 'T-Shirt and Sandals'
elif time.lower() == 'afternoon':
    if 10 <= degrees <= 18:
        outfit = 'Shirt and Moccasins'
    elif 18 < degrees <= 24:
        outfit = 'T-Shirt and Sandals'
    else:
        outfit = 'Swim Suit and Barefoot'
else:
    outfit = 'Shirt and Moccasins'

print(f"It's {degrees} degrees, get your {outfit}.")