budget = float(input())
season = input()
destination = ''
logging = ''

if season.lower() == 'summer':
    logging = 'Camp'
    if budget <= 100:
        destination = 'Bulgaria'
        budget = budget * 0.3
    elif budget <= 1000:
        destination = 'Balkans'
        budget = budget * 0.4
    else:
        destination = 'Europe'
        logging = 'Hotel'
        budget = budget * 0.9
else:
    logging = 'Hotel'
    if budget <= 100:
        destination = 'Bulgaria'
        budget = budget * 0.7
    elif budget <= 1000:
        destination = 'Balkans'
        budget = budget * 0.8
    else:
        destination = 'Europe'
        budget = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{logging} - {budget:.2f}")