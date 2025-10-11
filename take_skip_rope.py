def take_skip(take, skip):
    result = []
    if take > 0:
        result = non_digit_list[:take]
        non_digit_list[:take] = []

    if skip > 0:
        non_digit_list[:skip] = []

    return result


initial_string = input()

digit_list = []
non_digit_list = []
final_list = []

for element in initial_string:
    if element.isdigit():
        digit_list.append(element)
    else:
        non_digit_list.append(element)

take_list = []
skip_list = []

for index in range(len(digit_list)):
    if index % 2 == 0:
        take_list.append(digit_list[index])
    else:
        skip_list.append(digit_list[index])

for index in range(len(take_list)):
    final_list += take_skip(int(take_list[index]), int(skip_list[index]))

print("".join(final_list))