budget = float(input())
season = input()
type = ""
car = ""

if season.lower() == 'summer':
    if budget <= 100:
        type = 'Economy class'
        budget = budget * 0.35
        car = 'Cabrio'
    elif budget <= 500:
        type = 'Compact class'
        budget = budget * 0.45
        car = 'Cabrio'
    else:
        type = 'Luxury class'
        car = 'Jeep'
        budget = budget * 0.9
else:
    if budget <= 100:
        type = 'Economy class'
        budget = budget * 0.65
        car = 'Jeep'
    elif budget <= 500:
        type = 'Compact class'
        budget = budget * 0.8
        car = 'Jeep'
    else:
        type = 'Luxury class'
        car = 'Jeep'
        budget = budget * 0.9

print(type)
print(f"{car} - {budget:.2f}")