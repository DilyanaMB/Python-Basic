PUZZLE_PRICE = 2.6
DOLL_PRICE = 3.0
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2.0

vacation_price = float(input())
count_puzzles = int(input())
count_dolls = int(input())
count_teddy_bears = int(input())
count_minions = int(input())
count_trucks = int(input())

count_toys = count_puzzles + count_dolls + count_teddy_bears + count_minions + count_trucks
total_price_toys = ((count_puzzles * PUZZLE_PRICE)
                    + (count_dolls * DOLL_PRICE)
                    + (count_teddy_bears * TEDDY_BEAR_PRICE)
                    + (count_minions * MINION_PRICE)
                    + (count_trucks * TRUCK_PRICE))

if count_toys >= 50:
    total_price_toys -= total_price_toys * 0.25

total_price_toys -= total_price_toys * 0.1

if vacation_price <= total_price_toys:
    print(f"Yes! {total_price_toys - vacation_price:.2f} lv left.")
else:
    print(f"Not enough money! {abs(total_price_toys - vacation_price):.2f} lv needed.")
