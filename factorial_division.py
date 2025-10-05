def factorial_division(some_number) -> int:
    factorial_sum = some_number
    for digit in range(1, some_number):
        factorial_sum *= digit
    return factorial_sum

first_number = int(input())
second_number = int(input())

result = factorial_division(first_number) / factorial_division(second_number)
print(f"{result:.2f}")