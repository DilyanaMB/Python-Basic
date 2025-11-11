sec1 = int(input())
sec2 = int(input())
sec3 = int(input())

total_seconds = sec1 + sec2 + sec3
minutes = total_seconds // 60
seconds = total_seconds % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
