times = input().split()

integer_times = []

for digit in times:
    time = int(digit)
    integer_times.append(time)

middle_index = len(integer_times) // 2

left_time = 0
right_time = 0

for i in range(middle_index):
    left_time += integer_times[i]

    if integer_times[i] == 0:
        left_time = left_time * 0.8

for i in range(len(integer_times) - 1, middle_index, -1):
    right_time += integer_times[i]

    if integer_times[i] == 0:
        right_time = right_time * 0.8

if left_time < right_time:
    print(f"The winner is left with total time: {left_time:.1f}")
else:
    print(f"The winner is right with total time: {right_time:.1f}")