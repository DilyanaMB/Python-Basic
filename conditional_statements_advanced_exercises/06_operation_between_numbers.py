n1 = int(input())
n2 = int(input())
operator = input()
is_result_even = 'even'

if operator == "+":
    if (n1 + n2) % 2 != 0:
        is_result_even = 'odd'
    print(f"{n1} + {n2} = {n1 + n2} - {is_result_even}")
elif operator == "-":
    if (n1 - n2) % 2 != 0:
        is_result_even = 'odd'
    print(f"{n1} - {n2} = {n1 - n2} - {is_result_even}")
elif operator == "*":
    if (n1 * n2) % 2 != 0:
        is_result_even = 'odd'
    print(f"{n1} * {n2} = {n1 * n2} - {is_result_even}")
elif operator == "/":
    if n2 != 0:
        print(f"{n1} / {n2} = {n1 / n2:.2f}")
    else:
        print(f"Cannot divide {n1} by zero")
elif operator == "%":
    if n2 != 0:
        print(f"{n1} % {n2} = {n1 % n2}")
    else:
        print(f"Cannot divide {n1} by zero")
