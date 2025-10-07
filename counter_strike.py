initial_energy = int(input())

energy = initial_energy
win_count = 0

while True:
    command = input()

    if command == "End of battle":
        print(f"Won battles: {win_count}. Energy left: {energy}")
        break

    distance = int(command)

    if energy >= distance:
        win_count += 1
        energy -= distance
        if win_count % 3 == 0:
            energy += win_count

    else:
        print(f"Not enough energy! Game ends with {win_count} won battles and {energy} energy")
        break

