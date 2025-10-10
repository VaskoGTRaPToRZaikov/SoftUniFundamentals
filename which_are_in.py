first_sequences = input().split(", ")
second_sequences = input().split(", ")

new_list = []

for word in first_sequences:
    for any_word in second_sequences:
        if word in any_word:
            if word not in new_list:
                new_list.append(word)

print(new_list)