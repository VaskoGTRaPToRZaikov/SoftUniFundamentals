targets = list(map(int, input().split()))

shot_count = 0

while True:
    command = input()

    if command == "End":
        break

    index = int(command)

    if (index < 0 or index >= len(targets)
            or targets[index] == -1):
        continue

    shot_value = targets[index]

    targets[index] = -1
    shot_count += 1

    for i in range(len(targets)):
        if targets[i] != -1:
            if targets[i] > shot_value:
                targets[i] -= shot_value
            else:
                targets[i] += shot_value

print(f"Shot targets: {shot_count} -> {' '.join(map(str, targets))}")




