juniors_competitors = int(input())
seniors_competitors = int(input())
trace = input()
final_price = 0

if trace.lower() == 'trail':
    final_price = juniors_competitors * 5.5 + seniors_competitors * 7
elif trace.lower() == 'cross-country':
    final_price = juniors_competitors * 8 + seniors_competitors * 9.5
    if juniors_competitors + seniors_competitors >= 50:
        final_price -= final_price * 0.25
elif trace.lower() == 'downhill':
    final_price = juniors_competitors * 12.25 + seniors_competitors * 13.75
elif trace.lower() == 'road':
    final_price = juniors_competitors * 20 + seniors_competitors * 21.5

final_price -= final_price * 0.05
print(f"{final_price:.2f}")
