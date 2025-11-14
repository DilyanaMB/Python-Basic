VIP = 499.99
NORMAL = 249.99

budget = float(input())
category = input()
people = int(input())
travel_expenses = 0

if 4 >= people >= 1:
    travel_expenses = budget * 0.75
    budget -= budget * 0.75
elif 9 >= people > 4:
    travel_expenses = budget * 0.6
    budget -= budget * 0.6
elif 24 >= people > 9:
    travel_expenses = budget * 0.5
    budget -= budget * 0.5
elif 49 >= people > 24:
    travel_expenses = budget * 0.4
    budget -= budget * 0.4
elif people >= 50:
    travel_expenses = budget * 0.25
    budget -= budget * 0.25

needed_money_for_tickets = 0
if category.lower() == 'vip':
    needed_money_for_tickets = VIP * people
else:
    needed_money_for_tickets = NORMAL * people

if budget >= needed_money_for_tickets:
    print(f"Yes! You have {budget - needed_money_for_tickets:.2f} leva left.")
else:
    print(f"Not enough money! You need {needed_money_for_tickets - budget:.2f} leva.")
