import math
film = input()
film_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
relax_time = break_duration / 4

total_time_needed = lunch_time + relax_time + film_duration
time_difference = total_time_needed - break_duration

if total_time_needed > break_duration:
    print(
        f"You don't have enough time to watch {film}, "
        f"you need {abs(math.ceil(time_difference))} more minutes.")
else:
    print(
        f"You have enough time to watch {film} and left with {abs(math.ceil(time_difference))} minutes free time."
    )