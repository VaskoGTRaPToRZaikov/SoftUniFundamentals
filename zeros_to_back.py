single_string = input().split(", ")

number_list = []

for i in single_string:
    cleaning_space = i.strip()
    number = int(cleaning_space)
    number_list.append(number)

null_list = []
non_null_list = []

for num in number_list:
    if num == 0:
        null_list.append(num)
    else:
        non_null_list.append(num)

print(non_null_list + null_list)