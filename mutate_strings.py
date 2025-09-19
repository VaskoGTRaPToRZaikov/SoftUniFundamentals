first_string = input()
second_string = input()

for character_index in range(len(first_string)):
    left_side = second_string[:character_index + 1]
    right_side = first_string[character_index + 1:]
    new_string = left_side + right_side

    if first_string[character_index] != second_string[character_index]:
        print(new_string)




