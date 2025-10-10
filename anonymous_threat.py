def merge_elements(some_text, index_start, index_end):
    if index_start < 0:
        index_start = 0
    if index_end > len(some_text) - 1:
        index_end = len(some_text) - 1
    merge_text = ""
    for i in range(index_start, index_end + 1):
        merge_text += some_text[i]

    some_text = some_text[:index_start] + [merge_text] + some_text[index_end + 1:]
    return some_text

def divide_elements(some_text, divide_index, partition):
    element = some_text[divide_index]

    partition_size = len(element) // partition

    divided_parts = []

    for i in range(partition - 1):
        current_partition = element[i * partition_size:(i + 1) * partition_size]
        divided_parts.append(current_partition)

    divided_parts.append(element[(partition - 1) * partition_size:])

    some_text = some_text[:divide_index] + divided_parts + some_text[divide_index + 1:]
    return some_text


text = input().split()

while True:
    command = input().split()

    if command[0] == "3:1":
        break

    action = command[0]

    if action == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        text = merge_elements(text, start_index, end_index)



    elif action == "divide":
        index = int(command[1])
        partitions = int(command[2])
        text = divide_elements(text, index, partitions)



print(" ".join(text))


