width = float(input()) * 100
height = float(input()) * 100

CORRIDOR = 100

height -= CORRIDOR
desks_height= height // 70
desks_width = width // 120

possible_desks = desks_height * desks_width -3
print(possible_desks)
