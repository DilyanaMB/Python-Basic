figure = input()

if figure == 'square':
    side = float(input())
    area = side * side
    print(area)
if figure == 'triangle':
    side = float(input())
    height = float(input())
    area = (side * height) / 2
    print(area)
elif figure == 'circle':
    radius = float(input())
    area = 3.14159 * radius * radius
    print(area)
elif figure == 'rectangle':
    height = float(input())
    base = float(input())
    area = height * base
    print(area)
else:
    print("Unknown figure")
