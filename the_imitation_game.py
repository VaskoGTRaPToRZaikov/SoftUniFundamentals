code = input()

while True:
    command = input()

    if command == "Decode":
        break

    parts = command.split("|")
    action = parts[0]

    if action == "Move":
        number_of_letters = int(parts[1])
        code = code[number_of_letters:] + code[:number_of_letters]

    elif action == "Insert":
        index = int(parts[1])
        value = parts[2]
        code = code[:index] + value + code[index:]

    elif action == "ChangeAll":
        substring = parts[1]
        replacement = parts[2]

        code = code.replace(substring, replacement)

print(f"The decrypted message is: {code}")