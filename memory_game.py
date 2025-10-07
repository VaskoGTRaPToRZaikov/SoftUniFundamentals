elements = input().split()

number_of_moves = 0
while True:
    command = input()

    if command == "end":
        print(f"Sorry you lose :(")
        print(' '.join(elements))
        break

    parts = command.split()
    index1 = int(parts[0])
    index2 = int(parts[1])

    if (index1 == index2 or index1 >= len(elements) or
            index2 >= len(elements) or index1 < 0 or index2 < 0):
        number_of_moves += 1
        print("Invalid input! Adding additional elements to the board")
        middle_of_elements = len(elements) // 2
        element_to_add = f"-{number_of_moves}a"
        elements.insert(middle_of_elements, element_to_add)
        elements.insert(middle_of_elements, element_to_add)
        continue


    if elements[index1] == elements[index2]:
        print(f"Congrats! You have found matching elements - {elements[index1]}!")
        if index1 > index2:
            elements.pop(index1)
            elements.pop(index2)
        else:
            elements.pop(index2)
            elements.pop(index1)
    elif elements[index1] != elements[index2]:
        print("Try again!")

    number_of_moves += 1

    if len(elements) == 0:
        print(f"You have won in {number_of_moves} turns!")
        break

