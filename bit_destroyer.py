n = int(input())
p = int(input())

mask = 1 << p

mask = ~mask

new_number = n & mask

print(new_number)