fruit = input()
day = input()
quantity = float(input())
price = 0
is_valid = True

if day.lower() == 'saturday' or day.lower() == 'sunday':
    match fruit:
        case 'banana':
            price = quantity * 2.7
        case 'apple':
            price = quantity * 1.25
        case 'orange':
            price = quantity * 0.9
        case 'grapefruit':
            price = quantity * 1.6
        case 'kiwi':
            price = quantity * 3.0
        case 'pineapple':
            price = quantity * 5.6
        case 'grapes':
            price = quantity * 4.2
        case _:
            print('error')
            is_valid = False
    if is_valid:
        print(f"{price:.2f}")

elif (day.lower() == 'monday' or day.lower() == 'tuesday'
      or day.lower() == 'wednesday' or day.lower() == 'thursday' or day.lower() == 'friday'):
    match fruit:
        case 'banana':
            price = quantity * 2.5
        case 'apple':
            price = quantity * 1.2
        case 'orange':
            price = quantity * 0.85
        case 'grapefruit':
            price = quantity * 1.45
        case 'kiwi':
            price = quantity * 2.7
        case 'pineapple':
            price = quantity * 5.5
        case 'grapes':
            price = quantity * 3.85
        case _:
            print('error')
            is_valid = False

    if is_valid:
        print(f"{price:.2f}")

else:
    print('error')
