targets = list(map(int, input().split()))

while True:
    commands = input()

    if commands == "End":
        print("|".join(map(str,targets)))
        break

    parts = commands.split()
    action = parts[0]
    index = int(parts[1])

    if index < 0 or index >= len(targets):
        if action == "Add":
            print("Invalid placement!")
        continue

    if action == "Shoot":
        power = int(parts[2])
        targets[index] -= power

        if targets[index] <= 0:
            targets.pop(index)

    elif action == "Add":
        value = int(parts[2])
        targets.insert(index, value)

    elif action == "Strike":
        radius = int(parts[2])

        if (index - radius) < 0 or (index + radius) >= len(targets):
            print("Strike missed!")
            continue
        start_index = index - radius
        end_index = index + radius
        del targets[start_index:end_index + 1]





