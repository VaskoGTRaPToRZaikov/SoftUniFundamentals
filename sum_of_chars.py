number_of_chars = int(input())

total_sum = 0

for _ in range(number_of_chars):
    character = input()
    total_sum += ord(character)

print(f"The sum equals: {total_sum}")