season = input()
type = input()
students_count = int(input())
nights_to_stay = int(input())
price = 0.0

if type.lower() == 'boys' or type.lower() == 'girls':
    if season.lower() == 'winter':
        price = nights_to_stay * 9.6 * students_count
    elif season.lower() == 'spring':
        price = nights_to_stay * 7.2 * students_count
    else:
        price = nights_to_stay * 15.0 * students_count
else:
    if season.lower() == 'winter':
        price = nights_to_stay * 10.0 * students_count
    elif season.lower() == 'spring':
        price = nights_to_stay * 9.5 * students_count
    else:
        price = nights_to_stay * 20.0 * students_count

if students_count >= 50:
    price -= price * 0.5
elif students_count >= 20:
    price -= price * 0.15
elif 10 <= students_count <= 20:
    price -= price * 0.05

sport = ''

if type.lower() == 'girls':
    if season.lower() == 'winter':
        sport = 'Gymnastics'
    elif season.lower() == 'spring':
        sport = 'Athletics'
    else:
        sport = 'Volleyball'
elif type.lower() == 'boys':
    if season.lower() == 'winter':
        sport = 'Judo'
    elif season.lower() == 'spring':
        sport = 'Tennis'
    else:
        sport = 'Football'
else:
    if season.lower() == 'winter':
        sport = 'Ski'
    elif season.lower() == 'spring':
        sport = 'Cycling'
    else:
        sport = 'Swimming'

print(f"{sport} {price:.2f} lv.")
