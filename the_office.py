happiness_list = list(map(int, input().split()))
improvement_factor = int(input())

improved_list = list(map(lambda x: x * improvement_factor, happiness_list))
average_happiness = sum(happiness_list) / len(happiness_list)
happy_count = list(filter(lambda x: x >= (sum(happiness_list) / len(happiness_list)), happiness_list))

if len(happy_count) >= len(happiness_list) / 2:
    print(f"Score: {len(happy_count)}/{len(happiness_list)}. Employees are happy!")
else:
    print(f"Score: {len(happy_count)}/{len(happiness_list)}. Employees are not happy!")