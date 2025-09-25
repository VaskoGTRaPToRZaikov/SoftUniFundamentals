number = int(input())
magic_word = input()

main_list = []
filtered_list = []

for _ in range(number):
    string = input()
    main_list.append(string)

for i in range(len(main_list)):
    current_string = main_list[i]

    if magic_word in current_string:
        filtered_list.append(current_string)

print(main_list)
print(filtered_list)