n = int(input())
p = int(input())

shifted = n >> p

bit_at_position_1 = shifted & 1

print(bit_at_position_1)