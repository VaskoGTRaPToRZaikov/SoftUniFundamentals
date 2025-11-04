n = int(input())
b = input()

binary_n = bin(n)[2:]
count_b = binary_n.count(b)

print(count_b)
