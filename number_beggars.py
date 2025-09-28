money_string = input().split(", ")
number_of_beggars = int(input())

integer_money = []

for money in money_string:
    integer_money.append(int(money))

beggars_sum = []
start_index = 0

for current_beggar in range(number_of_beggars):
    current_beggar_sum = 0

    for index in range(start_index, len(integer_money), number_of_beggars):
        current_beggar_sum += integer_money[index]

    beggars_sum.append(current_beggar_sum)
    start_index += 1

print(beggars_sum)


