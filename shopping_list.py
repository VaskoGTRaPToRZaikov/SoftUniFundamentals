initial_list = input().split("!")

while True:
    command = input()

    if command == "Go Shopping!":
        print(", ".join(initial_list))
        break

    commands = command.split()
    action = commands[0]
    item = commands[1]

    if action == "Urgent":

        if item not in initial_list:
            initial_list.insert(0, item)
        else:
            continue

    elif action == "Unnecessary":

        if item in initial_list:
            initial_list.remove(item)
        else:
            continue

    elif action == "Correct":
        old_item = item
        new_item = commands[2]

        if old_item in initial_list:
            old_index = initial_list.index(old_item)
            initial_list.pop(old_index)
            initial_list.insert(old_index, new_item)
        else:
            continue

    elif action == "Rearrange":

            if item in initial_list:
                initial_list.remove(item)
                initial_list.append(item)
            else:
                continue
