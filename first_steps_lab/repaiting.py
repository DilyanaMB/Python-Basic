NYLON = 1.5
PAINT = 14.5
THINNER = 5.0
BAGS = 0.4

nylon_sq_m = int(input())
paint_litters = int(input())
thinner_litters = int(input())
working_hours = int(input())

paint_litters += paint_litters * 0.1
nylon_sq_m += 2

materials = (nylon_sq_m * NYLON) + (paint_litters * PAINT) + (thinner_litters * THINNER) + BAGS
workers_fee = (materials * 0.3) * working_hours

print(materials + workers_fee)
