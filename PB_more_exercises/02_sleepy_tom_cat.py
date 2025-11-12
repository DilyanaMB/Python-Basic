vacation_days = int(input())
TOTAL_DAYS = 365
TOM_PLAYING_TIME_LIMIT = 30000

working_days = TOTAL_DAYS - vacation_days
total_play_time = working_days * 63 + vacation_days * 127

difference = total_play_time - TOM_PLAYING_TIME_LIMIT
hours = abs(difference) // 60
minutes = abs(difference) % 60

if difference > 0:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
