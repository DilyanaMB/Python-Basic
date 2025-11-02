pages = int(input())
pages_per_hour = int(input())
days_for_book = int(input())

necessary_hours_to_read_book = pages // pages_per_hour
necessary_hours_per_day = necessary_hours_to_read_book // days_for_book

print(necessary_hours_per_day)
