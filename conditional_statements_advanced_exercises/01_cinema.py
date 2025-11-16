PREMIERE_PRICE = 12.0
NORMAL_PRICE = 7.5
DISCOUNT_PRICE = 5.0

type = input()
r = int(input())
c = int(input())

total_ticket_price =0
if type.lower() == 'premiere':
    total_ticket_price = PREMIERE_PRICE * r * c
elif type.lower() == 'normal':
    total_ticket_price = NORMAL_PRICE * r * c
elif type.lower() == 'discount':
    total_ticket_price = DISCOUNT_PRICE * r * c

print(f"{total_ticket_price:.2f} leva")