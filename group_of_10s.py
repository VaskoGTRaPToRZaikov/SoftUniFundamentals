sequence_of_numbers = [int(number) for number in input().split(", ")]

current_group = 10

while sequence_of_numbers:

    current_list = []

    for number in sequence_of_numbers:
        if number <= current_group:
            current_list.append(number)

    print(f"Group of {current_group}'s: {current_list}")

    sequence_of_numbers = [number for number in sequence_of_numbers if number not in current_list]

    current_group += 10
