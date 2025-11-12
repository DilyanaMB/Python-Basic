import math

x_sq_m = int(input())
y_grape_per_sq_m = float(input())
z_needed_litters_wine = int(input())
workers = int(input())
NEEDED_KG_GRAPE_FOR_LITTER_WINE = 2.5

total_grape = x_sq_m * y_grape_per_sq_m
wine = 0.4 * total_grape / NEEDED_KG_GRAPE_FOR_LITTER_WINE

if wine >= z_needed_litters_wine:
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    wine_left = wine - z_needed_litters_wine
    wine_per_worker = (wine - z_needed_litters_wine) / workers
    print(f"{math.ceil(wine_left)} liters left -> {math.ceil(wine_per_worker)} liters per person.")
else:
    needed_wine=z_needed_litters_wine-wine
    print(f"It will be a tough winter! More {math.floor(needed_wine)} liters wine needed.")