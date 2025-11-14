product = input()
city = input()
quantity = float(input())
price = 0.0

if product == 'coffee':
    if city == 'Sofia':
        price = quantity * 0.5
    elif city == 'Plovdiv':
        price = quantity * 0.4
    else:
        price = quantity * 0.45
elif product == 'water':
    if city == 'Sofia':
        price = quantity * 0.8
    else:
        price = quantity * 0.7
elif product == 'beer':
    if city == 'Sofia':
        price = quantity * 1.2
    elif city == 'Plovdiv':
        price = quantity * 1.15
    else:
        price = quantity * 1.1
elif product == 'sweets':
    if city == 'Sofia':
        price = quantity * 1.45
    elif city == 'Plovdiv':
        price = quantity * 1.3
    else:
        price = quantity * 1.35
else:
    if city == 'Sofia':
        price = quantity * 1.6
    elif city == 'Plovdiv':
        price = quantity * 1.5
    else:
        price = quantity * 1.55

print(price)
