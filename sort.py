numbers_string = input().split()
numbers_as_digits = []

for digit in numbers_string:
    numbers_as_digits.append(int(digit))

result = list(sorted(numbers_as_digits))
print(result)