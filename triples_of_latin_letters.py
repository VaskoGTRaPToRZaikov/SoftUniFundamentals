number_of_letters = int(input())

for index_one in range(97, 97 + number_of_letters):
    for index_two in range(97, 97 + number_of_letters):
        for index_three in range(97, 97 + number_of_letters):
            print(f"{chr(index_one)}{chr(index_two)}{chr(index_three)}")