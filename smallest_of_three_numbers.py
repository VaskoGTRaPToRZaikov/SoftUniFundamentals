def smallest_number(num1, num2, num3) -> int:
    return min(num1, num2, num3)

first_integer = int(input())
second_integer = int(input())
third_integer = int(input())

result = smallest_number(first_integer, second_integer, third_integer)

print(result)