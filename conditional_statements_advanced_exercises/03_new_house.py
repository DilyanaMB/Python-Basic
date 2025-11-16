ROSES_PRICE = 5.0
DAHLIAS_PRICE = 3.8
TULIPS_PRICE = 2.8
NARCISSUS_PRICE = 3.0
GLADIOLUS_PRICE = 2.5

type = input()
flowers_count = int(input())
budget = float(input())
total_cost = 0

if type.lower() == 'roses':
    total_cost = ROSES_PRICE * flowers_count
    if flowers_count > 80:
        total_cost -= total_cost * 0.1
elif type.lower() == 'dahlias':
    total_cost = DAHLIAS_PRICE * flowers_count
    if flowers_count > 90:
        total_cost -= total_cost * 0.15
elif type.lower() == 'tulips':
    total_cost = TULIPS_PRICE * flowers_count
    if flowers_count > 80:
        total_cost -= total_cost * 0.15
elif type.lower() == 'narcissus':
    total_cost = NARCISSUS_PRICE * flowers_count
    if flowers_count < 120:
        total_cost += total_cost * 0.15
elif type.lower() == 'gladiolus':
    total_cost = GLADIOLUS_PRICE * flowers_count
    if flowers_count < 80:
        total_cost += total_cost * 0.2

if budget >= total_cost:
    print(f"Hey, you have a great garden with {flowers_count} {type} and {budget-total_cost:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_cost-budget:.2f} leva more.")
