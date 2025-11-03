annual_tax = int(input())

basketball_snickers = annual_tax - (annual_tax * 0.4)
basketball_suit = basketball_snickers - (basketball_snickers * 0.2)
basketball_ball = basketball_suit * 0.25
basketball_accessories = basketball_ball * 0.2

sum = basketball_snickers + basketball_suit + basketball_ball + basketball_accessories + annual_tax

print(sum)
