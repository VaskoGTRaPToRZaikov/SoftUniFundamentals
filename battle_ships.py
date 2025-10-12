rows_of_the_field = int(input())

field = []

for i in range(rows_of_the_field):
    row = [int(num) for num in input().split()]
    field.append(row)

attacks = input().split()
destroyed_ships = 0

for attack in attacks:
    parts = attack.split("-")
    row = int(parts[0])
    col = int(parts[1])

    if field[row][col] > 0:
        field[row][col] -= 1
        if field[row][col] == 0:
            destroyed_ships += 1

print(destroyed_ships)
