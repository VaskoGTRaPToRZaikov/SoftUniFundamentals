def flip(code, some_case, index1, index2):
    changes = code[index1:index2]
    if some_case == "Upper":
        changes = changes.upper()
    elif some_case == "Lower":
        changes = changes.lower()
    code = code[:index1] + changes + code[end_index:]
    return code

raw_code = input()

while True:
    command = input()

    if command == "Generate":
        break

    parts = command.split(">>>")
    action = parts[0]

    if action == "Contains":
        substring = parts[1]
        if substring in raw_code:
            print(f"{raw_code} contains {substring}")
        else:
            print("Substring not found!")

    elif action == "Flip":
        case, start_index, end_index = parts[1], int(parts[2]), int(parts[3])
        raw_code = flip(raw_code, case, start_index, end_index)
        print(raw_code)

    elif action == "Slice":
        start_index, end_index = int(parts[1]), int(parts[2])
        raw_code = raw_code[:start_index] + raw_code[end_index:]
        print(raw_code)

print(f"Your activation key is: {raw_code}")