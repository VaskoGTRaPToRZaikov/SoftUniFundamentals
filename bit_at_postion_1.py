n = int(input())

shifted = n >> 1

bit_at_position_1 = shifted & 1

print(bit_at_position_1)