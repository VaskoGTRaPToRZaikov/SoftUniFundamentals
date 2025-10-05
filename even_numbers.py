def is_even(number) -> bool:
    return number % 2 == 0

numbers_string = input().split()
numbers_as_digits = []
for num in numbers_string:
    numbers_as_digits.append(int(num))
result = list(filter(is_even, numbers_as_digits))
print(result)

