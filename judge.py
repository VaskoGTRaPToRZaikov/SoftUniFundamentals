data = {}
contests = {}
students_total_points = {}
input_order_contests = []

while True:
    command = input()

    if command == "no more time":
        break

    information = command.split(" -> ")
    username = information[0]
    contest = information[1]
    points = int(information[2])

    if username not in data.keys():
        data[username] = {}
        students_total_points[username] = 0

    if contest not in data[username]:
        data[username][contest] = points
        students_total_points[username] += points

    else:
        if points > data[username][contest]:
            difference = points - data[username][contest]
            data[username][contest] = points
            students_total_points[username] += difference

    if contest not in contests:
        contests[contest] = {}
        input_order_contests.append(contest)
    contests[contest][username] = data[username][contest]

for this_contest in input_order_contests:
    participants = contests[this_contest]
    print(f"{this_contest}: {len(participants)} participants")

    sorted_participants = sorted(participants.items(), key=lambda x: (-x[1], x[0]))

    position = 1
    for name, score in sorted_participants:
        print(f"{position}. {name} <::> {score}")
        position += 1

print("Individual standings:")

sorted_students = sorted(students_total_points.items(), key=lambda x: (-x[1], x[0]))

position = 1
for name, total_points in sorted_students:
    print(f"{position}. {name} -> {total_points}")
    position += 1

