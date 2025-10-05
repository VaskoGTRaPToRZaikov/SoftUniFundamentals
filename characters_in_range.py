def characters_in_range(index1, index2):
    character_list = []
    for char in range(ord(index1) + 1, ord(index2)):
        character_list.append(chr(char))
    return character_list


first_character = input()
second_character = input()

result = characters_in_range(first_character, second_character)
print(" ".join(result))