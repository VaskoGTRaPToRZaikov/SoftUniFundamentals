number_strings = int(input())

for _ in range(number_strings):
    current_string = input()

    for char in current_string:

        if char == "," or char == "." or char == "_":
            print(f"{current_string} is not pure!")
            break

    else:
        print(f"{current_string} is pure.")

