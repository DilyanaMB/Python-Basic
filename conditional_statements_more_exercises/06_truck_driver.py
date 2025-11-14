season = input()
km_per_month = float(input())
salary = 0.0

if season.lower() == 'spring' or season.lower() == 'autumn':
    if km_per_month <= 5000:
        salary = km_per_month * 0.75 * 4
    elif km_per_month <= 10000:
        salary = km_per_month * 0.95 * 4
    else:
        salary = km_per_month * 1.45 * 4
elif season.lower() == 'summer':
    if km_per_month <= 5000:
        salary = km_per_month * 0.9 * 4
    elif km_per_month <= 10000:
        salary = km_per_month * 1.1 * 4
    else:
        salary = km_per_month * 1.45 * 4
else:
    if km_per_month <= 5000:
        salary = km_per_month * 1.05 * 4
    elif km_per_month <= 10000:
        salary = km_per_month * 1.25 * 4
    else:
        salary = km_per_month * 1.45 * 4

salary -= salary * 0.1
print(f"{salary:.2f}")
