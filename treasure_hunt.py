def loot(some_treasure_chest:list , some_items:list) -> list:
    for item in some_items:
        if item in some_treasure_chest:
            continue
        else:
            some_treasure_chest.insert(0, item)
    return some_treasure_chest

def drop(some_treasure_chest:list, some_index:int) -> list:
    removed_item = some_treasure_chest.pop(some_index)
    some_treasure_chest.append(removed_item)
    return some_treasure_chest

def steal(some_treasure_chest:list, some_count:int) -> list:
    if len(some_treasure_chest) <= some_count:
        print(", ".join(some_treasure_chest))
        some_treasure_chest = []
    else:
        last_new_index = len(some_treasure_chest) - some_count
        print(", ".join(some_treasure_chest[last_new_index:]))
        some_treasure_chest = some_treasure_chest[:last_new_index]

    return some_treasure_chest

treasure_chest = input().split("|")

while True:
    command = input()

    if command == "Yohoho!":
        break

    actions = command.split()
    action = actions[0]

    if action == "Loot":
        items = actions[1:]
        treasure_chest = loot(treasure_chest, items)

    elif action == "Drop":
        index = int(actions[1])
        if 0 <= index < len(treasure_chest):
            treasure_chest = drop(treasure_chest, index)

    elif action == "Steal":
        count = int(actions[1])
        treasure_chest = steal(treasure_chest, count)

if treasure_chest:
    average_gain =sum(len(item) for item in treasure_chest) / len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")