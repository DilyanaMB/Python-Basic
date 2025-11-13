GASOLINE = 2.22
DIESEL = 2.33
GAS = 0.93

type = input()
fuel_litters = float(input())
club_card = input()
has_club_card = False


if club_card.lower() == 'yes':
    has_club_card = True
    GASOLINE -= 0.18
    DIESEL -= 0.12
    GAS -= 0.08

price =0
if type.lower() == 'gasoline':
    price = GASOLINE * fuel_litters
elif type.lower() == 'diesel':
    price = DIESEL * fuel_litters
elif type.lower() == 'gas':
    price = GAS* fuel_litters

if 25 >= fuel_litters >= 20:
    price = price - (price*0.08)
elif fuel_litters >= 25:
    price = price - (price*0.1)

print(f"{price:.2f} lv.")