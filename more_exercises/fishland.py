mackerel_price = float(input())
safrid_price = float(input())
bonito_kg = float(input())
safrid_kg = float(input())
clams_kg = int(input())

CLAMS_PRICE = 7.5

bonito_price = mackerel_price + (mackerel_price * 0.6)
safrid_price = safrid_price + (safrid_price * 0.8)

total_price = (bonito_kg * bonito_price ) + (safrid_kg * safrid_price) + (CLAMS_PRICE * clams_kg)
print(f"{total_price:.2f}")