travel_route_to_titan = input().split("||")
fuel = int(input())
ammunition = int(input())


for part in travel_route_to_titan:
    commands = part.split()
    command = commands[0]

    if command == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break

    value = int(commands[1])

    if command == "Travel":
        light_years = value
        if fuel >= light_years:
            fuel -= light_years
            print(f"The spaceship travelled {light_years} light-years.")
        else:
            print("Mission failed.")
            break

    elif command == "Enemy":
        enemy_armor = value
        if ammunition >= enemy_armor:
            ammunition -= enemy_armor
            print(f"An enemy with {enemy_armor} armour is defeated.")
        else:
            fuel -= enemy_armor * 2
            if fuel > 0:
                print(f"An enemy with {enemy_armor} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break

    elif command == "Repair":
        fuel += value
        ammunition += value * 2
        print(f"Ammunitions added: {value * 2}.")
        print(f"Fuel added: {value}.")
