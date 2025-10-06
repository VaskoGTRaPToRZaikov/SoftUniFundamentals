collecting_items = input().split(", ")
inventory = collecting_items

while True:
    command = input()

    if command == "Craft!":
        print(", ".join(inventory))
        break

    actions = command.split(" - ")
    action = actions[0]
    item = actions[1]

    if action == "Collect":

        if item not in inventory:
            inventory.append(item)
        else:
            continue

    elif action == "Drop":

        if item in inventory:
            inventory.remove(item)
        else:
            continue

    elif action == "Combine Items":
        items = item.split(":")
        old_item = items[0]
        new_item = items[1]

        if old_item in inventory:
            old_index = inventory.index(old_item)
            inventory.insert(old_index + 1, new_item)
        else:
            continue

    elif action == "Renew":
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)
