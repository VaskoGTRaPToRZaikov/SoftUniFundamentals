factor = int(input())
count = int(input())

result_list = []

for multiplier in range(1, count + 1):
    result_list.append(factor * multiplier)

print(result_list)