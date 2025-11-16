exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes

if exam_time < arrival_time:
    print("Late")
    diff =  arrival_time-exam_time
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        diff_hours = diff // 60
        diff_minutes = diff % 60
        if diff_minutes<10:
            print(f"{diff_hours}:0{diff_minutes} hours after the start")
        else:
            print(f"{diff_hours}:{diff_minutes} hours after the start")
elif exam_time == arrival_time:
    print("On time")
else:
    diff = exam_time - arrival_time
    is_early = True if diff > 30 else False
    if diff < 60:
        if is_early:
            print("Early")
        else:
            print("On time")
        print(f"{diff} minutes before the start")
    else:
        if is_early:
            print("Early")
        else:
            print("On time")
        diff_hours = diff // 60
        diff_minutes = diff % 60
        if diff_minutes<10:
            print(f"{diff_hours}:0{diff_minutes} hours before the start")
        else:
            print(f"{diff_hours}:{diff_minutes} hours before the start")