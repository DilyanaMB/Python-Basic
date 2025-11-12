vacation_days = int(input())
TOTAL_DAYS = 365
TOM_PLAYING_TIME_LIMIT = 30000

working_days = TOTAL_DAYS - vacation_days
play_time_working_days = working_days * 63
play_time_non_working_days = vacation_days * 127

total_play_time = play_time_working_days + play_time_non_working_days

difference = TOM_PLAYING_TIME_LIMIT - total_play_time
hours = abs(difference) // 60
minutes = abs(difference) % 60

if TOM_PLAYING_TIME_LIMIT < total_play_time:
    print("Tom will run away")
    if minutes < 10:
        print(f"{hours} hours and 0{minutes} minutes more for play")
    else:
        print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    if minutes < 10:
        print(f"{hours} hours and 0{minutes} minutes less for play")
    else:
        print(f"{hours} hours and {minutes} minutes less for play")