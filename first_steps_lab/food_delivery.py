CHICKEN_MENU = 10.35
FISH_MENU = 12.4
VEGAN_MENU = 8.15
DELIVERY_PRICE = 2.5

count_chicken_menus = int(input())
count_fish_menus = int(input())
count_vegan_menus = int(input())

a=count_chicken_menus * CHICKEN_MENU
b=count_fish_menus * FISH_MENU
c=count_vegan_menus * VEGAN_MENU
sum = (count_chicken_menus * CHICKEN_MENU +
       count_fish_menus * FISH_MENU +
       count_vegan_menus * VEGAN_MENU)

desert = sum * 0.2

total_sum = sum + desert + DELIVERY_PRICE

print(total_sum)