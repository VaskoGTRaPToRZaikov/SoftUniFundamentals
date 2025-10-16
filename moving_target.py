def shoot(targets:list, some_index:int, power:int) ->list:
    if 0 <= some_index < len(targets):
        targets[some_index] -= power
        if targets[some_index] <= 0:
            targets.pop(some_index)

    return targets

def add(targets:list, some_index:int, value:int) ->list:
    if 0 <= some_index < len(targets):
        targets.insert(some_index, value)
    else:
        print("Invalid placement!")

    return targets

def strike(targets:list, some_index:int, radius:int) ->list:
    if 0 <= (some_index - radius) < len(targets) and\
        0 <= (some_index + radius) < len(targets):
        index_before = some_index - radius
        index_after = some_index + radius
        before_radius = targets[:index_before]
        after_radius = targets[index_after + 1:]
        targets = before_radius + after_radius
    else:
        print("Strike missed!")

    return targets


sequence_of_targets = [int(number) for number in input().split()]

while True:
    command = input()

    if command == "End":
        break

    actions = command.split()
    action, index, parameter = actions[0], int(actions[1]), int(actions[2])

    if action == "Shoot":
        sequence_of_targets = shoot(sequence_of_targets, index, parameter)

    elif action == "Add":
        sequence_of_targets = add(sequence_of_targets, index, parameter)

    elif action == "Strike":
        sequence_of_targets = strike(sequence_of_targets, index, parameter)

print("|".join(map(str, sequence_of_targets)))



