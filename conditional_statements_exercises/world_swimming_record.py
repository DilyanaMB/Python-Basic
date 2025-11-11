world_record = float(input())
distance_in_meters = float(input())
time_for_1_meter = float(input())
count_slowing = 0

if distance_in_meters >= 15:
    count_slowing = distance_in_meters // 15

ivan_time = distance_in_meters * time_for_1_meter
additional_slowing = count_slowing * 12.5
ivan_time += additional_slowing

if ivan_time < world_record:
    print(f"Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(world_record - ivan_time):.2f} seconds slower.")