def perfect_number(some_number) -> bool:
    divisors_sum = 1
    for digit in range(2, int(some_number)):
        if int(some_number) % digit == 0:
            divisors_sum += digit
    return int(some_number) == divisors_sum


number = input()
result = perfect_number(number)
if result:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")