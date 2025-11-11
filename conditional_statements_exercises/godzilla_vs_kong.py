film_budget = float(input())
extras_count = int(input())
extra_costume_price_per_person = float(input())

decor = film_budget * 0.1
extra_costume_price = extra_costume_price_per_person * extras_count

if extras_count > 150:
    extra_costume_price -= extra_costume_price * 0.1

price_difference = film_budget - (decor + extra_costume_price)

if decor + extra_costume_price > film_budget:
    print(f"Not enough money!")
    print(f"Wingard needs {abs(price_difference):.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {abs(price_difference):.2f} leva left.")