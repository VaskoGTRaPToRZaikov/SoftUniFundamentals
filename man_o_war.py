pirate_ship_status = list(map(int, input().split(">")))
warship_status = list(map(int, input().split(">")))
maximum_health_capacity = int(input())

game_over = False

while True:
    command = input()

    if command == "Retire":
        break

    parts = command.split()
    action = parts[0]

    if action == "Fire":
        index = int(parts[1])
        damage = int(parts[2])

        if 0 <= index < len(warship_status):
            warship_status[index] -= damage

            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                game_over = True
                break

    elif action == "Defend":
        start_index = int(parts[1])
        end_index = int(parts[2])
        damage = int(parts[3])

        if 0 <= start_index < len(pirate_ship_status) \
            and 0 <= end_index < len(pirate_ship_status):

            for i in range(start_index, end_index + 1):
                pirate_ship_status[i] -= damage

                if pirate_ship_status[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    game_over = True
                    break

            if game_over:
                break

    elif action == "Repair":
        index = int(parts[1])
        health = int(parts[2])

        if 0 <= index < len(pirate_ship_status):
            pirate_ship_status[index] += health

            if pirate_ship_status[index] > maximum_health_capacity:
                pirate_ship_status[index] = maximum_health_capacity


    elif action == "Status":
        threshold = maximum_health_capacity * 0.20
        count = 0

        for section in pirate_ship_status:
            if section < threshold:
                count += 1

        print(f"{count} sections need repair.")

if not game_over:
    pirate_sum = sum(pirate_ship_status)
    warship_sum = sum(warship_status)
    print(f"Pirate ship status: {pirate_sum}")
    print(f"Warship status: {warship_sum}")


