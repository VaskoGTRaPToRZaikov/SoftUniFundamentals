def tribonacci_sequence(some_number):
    num1, num2, num3 = 1, 1, 2

    result = []

    for i in range(1, some_number + 1):
        if i == 1:
            result.append(num1)
        elif i == 2:
            result.append(num2)
        elif i == 3:
            result.append(num3)
        else:
            next_num = num1 + num2 + num3
            result.append(next_num)

            num1 = num2
            num2 = num3
            num3 = next_num

    return " ".join(map(str, result))

number = int(input())
print(tribonacci_sequence(number))