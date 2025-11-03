length = int(input())
wight = int(input())
height = int(input())
percent = float(input())/100

volume = (length * wight * height) * 0.001
necessary_litters = volume * (1-percent)
print(necessary_litters)