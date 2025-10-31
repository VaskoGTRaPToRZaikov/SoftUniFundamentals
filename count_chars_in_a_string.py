text = input()
character_dictionary = {}

for character in text:
    if character == " ":
        continue
    if character not in character_dictionary.keys():
        character_dictionary[character] = 0
    character_dictionary[character] += 1

for char, occurrences in character_dictionary.items():
    print(f"{char} -> {occurrences}")