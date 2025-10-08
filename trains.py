wagons = [0] * int(input())

while True:
    command = input().split()

    if command[0] == "End":
        print(wagons)
        break

    elif command[0] == "add":
        add_people = int(command[1])
        wagons[-1] += add_people

    elif command[0] == "insert":
        index = int(command[1])
        added_people = int(command[2])
        wagons[index] += added_people

    elif command[0] == "leave":
        index = int(command[1])
        leave_people = int(command[2])
        wagons[index] -= leave_people

