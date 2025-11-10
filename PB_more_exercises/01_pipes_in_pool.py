volume = int(input())
p1 = int(input())
p2 = int(input())
hours = float(input())

p1_filled = p1 * hours
p2_filled = p2 * hours

total_filled_percent = (p1_filled + p2_filled) / volume * 100
p1_filled_percent = p1_filled / (total_filled_percent * 0.1)
p2_filled_percent = p2_filled / (total_filled_percent * 0.1)
total_litters = p1_filled + p2_filled

if (total_litters <= volume):
    print(f"The pool is {total_filled_percent:.2f}% full. Pipe 1: {p1_filled_percent:.2f}%. Pipe 2:"
          f" {p2_filled_percent :.2f}%.")
else:
    print(f"For {hours} hours the pool overflows with {total_litters - volume:.2f} liters.")
