PRICE_PER_METER = 7.61
sq_meters = float(input())

price = sq_meters * PRICE_PER_METER

discount = price * 0.18

final_price = price - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")
