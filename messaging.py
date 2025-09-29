numbers = input().split()
string = list(input())

text = []

for num in numbers:
    digit_sum = 0

    for digit in num:
        digit_sum += int(digit)

    index = digit_sum % len(string)

    text.append(string[index])

    string.pop(index)

print("".join(text))
