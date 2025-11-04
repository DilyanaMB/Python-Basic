EURO = 1.94

vegetables_price = float(input())
fruits_price = float(input())
kg_vegetables = int(input())
kg_fruits = int(input())

sum = (vegetables_price * kg_vegetables + fruits_price * kg_fruits)
sum_in_euro = sum / EURO
print(f"{sum_in_euro:.2f}")
