number = int(input())

list_of_numbers = []
filtered_list = []

for _ in range(number):
    numbers = int(input())
    list_of_numbers.append(numbers)

command = input()

if command == "even":
    for num in list_of_numbers:
        if num % 2 == 0:
            filtered_list.append(num)

if command == "odd":
    for num in list_of_numbers:
        if num % 2 != 0:
            filtered_list.append(num)

if command == "negative":
    for num in list_of_numbers:
        if num < 0:
            filtered_list.append(num)

if command == "positive":
    for num in list_of_numbers:
        if num >= 0:
            filtered_list.append(num)

print(filtered_list)