def minimum(numbers) -> int:
    return min(numbers)

def maximum(numbers) -> int:
    return max(numbers)

def summary_numbers(numbers) -> int:
    return sum(numbers)

def min_max_sum(numbers):
    min_result = minimum(numbers)
    max_result = maximum(numbers)
    sum_result = summary_numbers(numbers)
    return (f"The minimum number is {min_result}\n"
            f"The maximum number is {max_result}\n"
            f"The sum number is: {sum_result}")

string_numbers = input().split()
numbers_as_digits = []

for digit in string_numbers:
    numbers_as_digits.append(int(digit))

result = min_max_sum(numbers_as_digits)
print(result)