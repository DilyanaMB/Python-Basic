chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
holiday = input()
total_price = 0
flower_count = chrysanthemums_count + roses_count + tulips_count

if season.lower() == 'spring' or season.lower() == 'summer':
    total_price = chrysanthemums_count * 2.0 + roses_count * 4.1 + tulips_count * 2.5
    if holiday.lower() == 'y':
        total_price *= 1.15

    if season.lower() == 'spring' and tulips_count > 7:
        total_price *= 0.95
else:
    total_price = chrysanthemums_count * 3.75 + roses_count * 4.5 + tulips_count * 4.15
    if holiday.lower() == 'y':
        total_price *= 1.15

    if season.lower() == 'winter' and roses_count >= 10:
        total_price *= 0.90

if flower_count > 20:
    total_price *= 0.80

total_price += 2.0

print(f"{total_price:.2f}")
