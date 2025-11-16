n1=int(input())
n2=int(input())
operator =input()

if operator == "+":
    print(n1+n2)
elif operator == "-":
    print(n1-n2)
elif operator == "*":
    print(n1*n2)
elif operator == "/":
    if n2!=0:
        print(n1/n2)
    else:
        print(f"Cannot divide {n1} by zero")