sequence_of_strings = input().strip().split()
total_sum = 0

for string in sequence_of_strings:
    front_letter = string[0]
    back_letter = string[-1]
    number = int(string[1:-1])
    if front_letter == front_letter.upper():
        letter_position = ord(front_letter) - 64
        total_sum += number / letter_position
    elif front_letter == front_letter.lower():
        letter_position = ord(front_letter) - 96
        total_sum += number * letter_position

    if back_letter == back_letter.upper():
        letter_position = ord(back_letter) - 64
        total_sum -= letter_position
    elif back_letter == back_letter.lower():
        letter_position = ord(back_letter) - 96
        total_sum += letter_position

print(f"{total_sum:.2f}")