def is_palindrome(number) -> bool:
    return number == number[::-1]

numbers = input().split(", ")
for number in numbers:
    print(is_palindrome(number))