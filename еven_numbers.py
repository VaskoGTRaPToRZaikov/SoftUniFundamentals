numbers = list(map(int, input().split(", ")))

even_indices = list(filter(lambda x: numbers[x] % 2 == 0, range(len(numbers))))

print(even_indices)