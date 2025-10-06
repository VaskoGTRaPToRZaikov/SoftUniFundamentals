initial_loot = input().split("|")
treasure_chest = initial_loot

while True:
    command = input()

    if command == "Yohoho!":
        break

    parts = command.split()
    action = parts[0]

    if action == "Loot":
        items = parts[1:]

        for item in items:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)

    elif action == "Drop":
        index = int(parts[1])

        if 0 <= index <= len(treasure_chest):

            item = treasure_chest.pop(index)
            treasure_chest.append(item)

    elif action == "Steal":
        count = int(parts[1])

        stolen_count = min(count, len(treasure_chest))
        stolen_items = treasure_chest[-stolen_count:]
        treasure_chest = treasure_chest[:-stolen_count] \
            if stolen_count > 0 else treasure_chest

        print(", ".join(stolen_items))

if len(treasure_chest) == 0:
    print("Failed treasure hunt.")
else:
    total_length = sum(len(item) for item in treasure_chest)
    average_gain = total_length / len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")