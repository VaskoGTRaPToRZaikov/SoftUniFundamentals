number_of_rooms = int(input())

total_free_chairs = 0

for room in range (1, number_of_rooms + 1):
    chair_number, visitors = input().split()
    difference = len(chair_number) - int(visitors)
    total_free_chairs += difference

    if len(chair_number) < int(visitors):
        print(f"{abs(difference)} more chairs needed in room {room}")

if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")