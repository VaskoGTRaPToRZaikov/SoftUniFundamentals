first_character = input()
second_character = input()
random_string = input()

total_value = 0

for code in range(ord(first_character) + 1, ord(second_character)):
    for char in random_string:
        if chr(code) == char:
            total_value += code

print(total_value)

