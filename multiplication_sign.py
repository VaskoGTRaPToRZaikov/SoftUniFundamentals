def multiplication_sign(num1, num2, num3):
    if num1 == 0 or num2 == 0 or num3 == 0:
        return "zero"

    negative_count = 0

    if num1 < 0:
        negative_count += 1
    if num2 < 0:
        negative_count += 1
    if num3 < 0:
        negative_count += 1

    if negative_count % 2 == 1:
        return "negative"
    return "positive"

number_one = int(input())
number_two = int(input())
number_three = int(input())

result = multiplication_sign(number_one, number_two, number_three)
print(result)