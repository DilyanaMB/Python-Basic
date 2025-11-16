SPRING_RENT = 3000.0
SUMMER_AUTUMN_RENT = 4200.0
WINTER_RENT = 2600.0

budget = float(input())
season = input()
fisherman = int(input())
total_price = 0

if season.upper() == 'SPRING':
    total_price = SPRING_RENT
elif season.upper() == 'SUMMER' or season.upper() == 'AUTUMN':
    total_price = SUMMER_AUTUMN_RENT
else:
    total_price = WINTER_RENT

if fisherman <= 6:
    total_price -= total_price * 0.1
elif fisherman <= 11:
    total_price -= total_price * 0.15
elif fisherman > 11:
    total_price -= total_price * 0.25

if season.upper() != 'AUTUMN' and fisherman % 2 == 0:
    total_price -= total_price * 0.05

if budget >= total_price:
    print(f"Yes! You have {budget-total_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_price-budget:.2f} leva.")