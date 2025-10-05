def add(num1, num2) -> int:
    sum_numbers = num1 + num2
    return sum_numbers

def subtract(sum_numbers, num3) -> int:
    some_result = sum_numbers - num3
    return some_result

def add_and_subtract(first_num, second_num, third_num) -> int:
    returned_result = add(first_num, second_num)
    final_result = subtract(returned_result, third_num)
    return final_result

first_number = int(input())
second_number = int(input())
third_number = int(input())

result = add_and_subtract(first_number, second_number, third_number)

print(result)