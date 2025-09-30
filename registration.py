username = input()

while True:
    instructions = input().split()
    command = instructions[0]

    if command == "Registration":
        break

    elif command == "Letters":
        letters = instructions[1]

        if letters == "Lower":
            username = username.lower()
            print(username)

        elif letters == "Upper":
            username = username.upper()
            print(username)

        else:
            continue

    elif command == "Reverse":
        start_index = int(instructions[1])
        end_index = int(instructions[2])

        if 0 <= start_index < end_index < len(username):
            substring = username[start_index:end_index + 1]
            rev_substring = substring[::-1]
            print(rev_substring)

        else:
            continue

    elif command == "Substring":
        substring = instructions[1]

        if substring in username:
            username = username.replace(substring, "", 1)
            print(username)

        else:
            print(f"The username {username} doesn't contain {substring}.")

    elif command == "Replace":
        char = instructions[1]

        if char in username:
            username = username.replace(char, "-")
            print(username)

        else:
            continue

    elif command == "IsValid":
        char = instructions[1]

        if char in username:
            print(f"Valid username.")

        else:
            print(f"{char} must be contained in your username.")





