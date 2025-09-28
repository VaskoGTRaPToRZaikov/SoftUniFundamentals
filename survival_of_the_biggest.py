import sys

numbers = input().split()
count_of_numbers = int(input())

integer_numbers = []

for number in numbers:
    integer_numbers.append(int(number))

for _ in range(count_of_numbers):
    removed_num = sys.maxsize

    for num in integer_numbers:
        if removed_num > num:
            removed_num = num

    integer_numbers.remove(removed_num)


print(", ".join(map(str, integer_numbers)))

