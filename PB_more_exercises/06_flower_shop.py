import math

MAGNOLIAS = 3.25
HYACINTHS = 4
ROSES = 3.5
CACTI = 8

count_magnolias = int(input())
count_hyacinths = int(input())
count_roses = int(input())
count_cacti = int(input())
present_price = float(input())

total_sum = ((count_magnolias * MAGNOLIAS)
             + (count_hyacinths * HYACINTHS)
             + (count_roses * ROSES)
             + (count_cacti * CACTI))

TAX = 0.05
total_sum -= total_sum * TAX

if total_sum >= present_price:
    money_left =  total_sum -present_price
    print(f"She is left with {math.floor(money_left)} leva.")
else:
    needed_money = present_price - total_sum
    print(f"She will have to borrow {math.ceil(needed_money)} leva.")