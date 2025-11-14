city = input()
sells_volume = float(input())
commission = 0
is_valid = True

match city:
    case 'Sofia':
        if 0 <= sells_volume <= 500:
            commission = sells_volume * 0.05
        elif 500 < sells_volume <= 1000:
            commission = sells_volume * 0.07
        elif 1000 < sells_volume <= 10000:
            commission = sells_volume * 0.08
        elif 10000 < sells_volume:
            commission = sells_volume * 0.12
        else:
            is_valid = False
    case 'Varna':
        if 0 <= sells_volume <= 500:
            commission = sells_volume * 0.045
        elif 500 < sells_volume <= 1000:
            commission = sells_volume * 0.075
        elif 1000 < sells_volume <= 10000:
            commission = sells_volume * 0.1
        elif 10000 < sells_volume:
            commission = sells_volume * 0.13
        else:
            is_valid = False
    case 'Plovdiv':
        if 0 <= sells_volume <= 500:
            commission = sells_volume * 0.055
        elif 500 < sells_volume <= 1000:
            commission = sells_volume * 0.08
        elif 1000 < sells_volume <= 10000:
            commission = sells_volume * 0.12
        elif 10000 < sells_volume:
            commission = sells_volume * 0.145
        else:
            is_valid = False
    case _:
        is_valid= False

if is_valid:
    print(f"{commission:.2f}")
else:
    print('error')