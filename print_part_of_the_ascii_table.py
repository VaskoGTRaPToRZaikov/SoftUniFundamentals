start_index = int(input())
last_index = int(input())

for char in range(start_index, last_index + 1):
    if char == last_index:
        print(chr(char))
    else:
        print(chr(char), end= " ")