ROOM_FOR_ONE_PERSON = 18.0
APARTMENT = 25.0
PRESIDENT_APARTMENT = 35.0

days= int(input())
logging = input()
rate = input()
is_positive_rate = True if rate == "positive" else False
total_price = 0

if logging =='room for one person':
    total_price = ROOM_FOR_ONE_PERSON * (days -1)
elif logging == 'apartment':
    total_price = APARTMENT * (days - 1)
    if days <10:
        total_price -= total_price * 0.3
    elif 10<=days<=15:
        total_price -= total_price * 0.35
    else:
        total_price -= total_price * 0.5
else:
    total_price = PRESIDENT_APARTMENT * (days - 1)
    if days <10:
        total_price -= total_price * 0.1
    elif 10<=days<=15:
        total_price -= total_price * 0.15
    else:
        total_price -= total_price * 0.2

if is_positive_rate:
    total_price += total_price * 0.25
else:
    total_price -= total_price * 0.1

print(f"{total_price:.2f}")