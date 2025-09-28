gifts = input().split()

while True:
    command_input = input().split()

    if " ".join(command_input) == "No Money":
        break

    command = command_input[0]

    if command == "OutOfStock":
        gift_to_remove = command_input[1]
        for index in range(len(gifts)):
            if gifts[index] == gift_to_remove:
                gifts[index] = "None"

    elif command == "Required":
        gift_to_replace = command_input[1]
        index_to_replace = int(command_input[2])

        if 0 <= index_to_replace < len(gifts):
            gifts[index_to_replace] = gift_to_replace

    elif command == "JustInCase":
        last_gift_to_replace = command_input[1]
        gifts[-1] = last_gift_to_replace

final_gifts = []
for gift in gifts:
   if gift != "None":
       final_gifts.append(gift)

# final_gifts = [gift for gift in gifts if gift != "None"]

print(" ".join(final_gifts))


