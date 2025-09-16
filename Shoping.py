budget = int(input())
total_cost = 0

while True:
    command = input()

    if command == "End":
        print("You bought everything needed.")
        break

    price = int(command)

    total_cost += price

    if total_cost > budget:
        print("You went in overdraft!")
        break