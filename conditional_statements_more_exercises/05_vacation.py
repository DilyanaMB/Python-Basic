budget = float(input())
season = input()
lodging =''
location = ''

if season.lower() == 'summer':
    if budget <=1000:
        lodging = 'Camp'
        location = 'Alaska'
        budget *= 0.65
    elif budget <=3000:
        lodging = 'Hut'
        location = 'Alaska'
        budget *= 0.8
    else:
        lodging = 'Hotel'
        location = 'Alaska'
        budget *= 0.9
else:
    if budget <=1000:
        lodging = 'Camp'
        location = 'Morocco'
        budget *= 0.45
    elif budget <=3000:
        lodging = 'Hut'
        location = 'Morocco'
        budget *= 0.6
    else:
        lodging = 'Hotel'
        location = 'Morocco'
        budget *= 0.9

print(f"{location} - {lodging} - {budget:.2f}")