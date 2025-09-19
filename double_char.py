double_char_string = ""

while True:
    command = input()

    if command == "End":
        break

    elif command == "SoftUni":
        continue

    else:
        current_string = command

        for char in current_string:
            double_char_string += 2 * char

    print(double_char_string)
    double_char_string = ""