n = int(input())
p = int(input())

mask = 7 << p

result = n ^ mask

print(result)