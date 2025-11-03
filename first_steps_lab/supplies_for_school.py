PACKAGE_PEN = 5.80
PACKAGE_MARKER = 7.20
DETERGENT = 1.20

count_package_pen = int(input())
count_package_marker = int(input())
liters_detergent = int(input())
percentage_discount = int(input())/100

sum = ((count_package_pen * PACKAGE_PEN) +
       (count_package_marker * PACKAGE_MARKER) +
       (liters_detergent * DETERGENT))
sum -= (sum * percentage_discount)

print(sum)
