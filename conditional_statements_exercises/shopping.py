peter_budget = float(input())
count_videocards = int(input())
count_cpu = int(input())
count_ram = int(input())

VIDEOCARD_PRICE = 250.0
videocard_price_total = VIDEOCARD_PRICE * count_videocards
cpu_price = videocard_price_total * 0.35
ram_price = videocard_price_total * 0.1

price = ((count_ram * ram_price) + (count_cpu * cpu_price)
         + videocard_price_total)

if count_videocards > count_cpu:
    price -= price * 0.15

difference = price - peter_budget

if peter_budget >= price:
    print(f"You have {abs(difference):.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(difference):.2f} leva more!")
