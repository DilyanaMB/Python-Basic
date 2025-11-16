MAY_OCT_STUDIO_PRICE = 50.0
MAY_OCT_APARTMENT_PRICE = 65.0
JUN_SEP_STUDIO_PRICE = 75.2
JUN_SEP_APARTMENT_PRICE = 68.7
JUL_AUG_STUDIO_PRICE = 76.0
JUL_AUG_APARTMENT_PRICE = 77.0

month = input()
nights = int(input())
total_price_studio = 0
total_price_apartment = 0

if month.lower() == 'may' or month.lower() == 'october':
    total_price_studio = MAY_OCT_STUDIO_PRICE * nights
    if 7 < nights <= 14:
        total_price_studio -= total_price_studio * 0.05
    elif 14 < nights:
        total_price_studio -= total_price_studio * 0.3
elif month.lower() == 'june' or month.lower() == 'september':
    total_price_studio = JUN_SEP_STUDIO_PRICE * nights
    if 14 < nights:
        total_price_studio -= total_price_studio * 0.2
elif month.lower() == 'july' or month.lower() == 'august':
    total_price_studio = JUL_AUG_STUDIO_PRICE * nights

if month.lower() == 'may' or month.lower() == 'october':
    total_price_apartment = MAY_OCT_APARTMENT_PRICE * nights
elif month.lower() == 'june' or month.lower() == 'september':
    total_price_apartment = JUN_SEP_APARTMENT_PRICE * nights

elif month.lower() == 'july' or month.lower() == 'august':
    total_price_apartment = JUL_AUG_APARTMENT_PRICE * nights

if  14 < nights:
    total_price_apartment -= total_price_apartment * 0.1

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")