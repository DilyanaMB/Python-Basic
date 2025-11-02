deposit = float(input())
deposit_trial_in_moths = int(input())
year_rate_percent = float(input()) * 0.01

sum = deposit + deposit_trial_in_moths * ((deposit * year_rate_percent) / 12)

print(sum)
