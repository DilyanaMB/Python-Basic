x = float(input())
y = float(input())
h = float(input())

door_area = 1.2 * 2
front_wall_area = x * x - door_area
back_wall_area = x * x
window_area = 1.5 * 1.5
side_wall_area = x * y - window_area
roof_rectangle_area = x * y
roof_triangle_area = (x * h) / 2

litters_green_paint = (front_wall_area + back_wall_area + 2 * side_wall_area)/3.4
litters_red_paint = (roof_triangle_area * 2 + roof_rectangle_area * 2)/4.3
print(f"{litters_green_paint:.2f}")
print(f"{litters_red_paint:.2f}")
