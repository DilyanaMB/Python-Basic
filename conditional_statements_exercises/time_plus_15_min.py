hour = int(input())
min = int(input())

total_time_in_minutes = hour * 60 + min + 15
total_hours = total_time_in_minutes // 60
total_minutes = total_time_in_minutes % 60

if total_hours > 23:
    total_hours -= 24

if total_minutes < 10:
    print(f"{total_hours}:0{total_minutes}")
else:
    print(f"{total_hours}:{total_minutes}")
