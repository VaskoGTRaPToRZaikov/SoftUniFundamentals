people = int(input())
wagons = list(map(int, input().split()))
remaining_people = people

for i in range(len(wagons)):
    if remaining_people == 0:
        break

    space = 4 - wagons[i]
    if space > 0:
        if space <= remaining_people:
            add = space
        else:
            add = remaining_people
        wagons[i] += add
        remaining_people -= add

has_empty_spots = any(wagon < 4 for wagon in wagons)

if remaining_people == 0:
    if has_empty_spots:
        print("The lift has empty spots!")
    print(' '.join(map(str, wagons)))
else:
    print(f"There isn't enough space! {remaining_people} people in a queue!")
    print(' '.join(map(str, wagons)))




