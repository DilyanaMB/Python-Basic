n = int(input())
time = input()

TAXI_PRICE = 0.7
TAXI_DAY_PRICE = 0.79
TAXI_NIGHT_PRICE = 0.9
BUS_PRICE = 0.09
TRAIN_PRICE = 0.06

price = 0

if n >= 100:
    price = TRAIN_PRICE * n
elif n >= 20:
    price = BUS_PRICE * n
else:
    price = TAXI_PRICE
    if time == 'day':
        price += TAXI_DAY_PRICE * n
    else:
        price += TAXI_NIGHT_PRICE * n

print(f"{price:.2f}")
