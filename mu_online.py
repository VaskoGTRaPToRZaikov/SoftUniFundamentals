dungeon_string = input().split("|")
total_health = 100
coins = 0
best_room = 0
is_complete = True

for rooms in dungeon_string:
    room = rooms.split()
    command = room[0]
    number = int(room[1])
    best_room += 1

    if command == "potion":
        current_health = total_health
        total_health += number
        if total_health > 100:
            total_health = 100
            healed_amount = total_health - current_health
        else:
            healed_amount = number

        print(f"You healed for {healed_amount} hp.")
        print(f"Current health: {total_health} hp.")

    elif command == "chest":
        coins += number
        print(f"You found {number} bitcoins.")

    else:
        total_health -= number

        if total_health <= 0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {best_room}")
            is_complete = False
            break
        else:
            print(f"You slayed {command}.")

if is_complete:
    print(f"You've made it!\nBitcoins: {coins}\nHealth: {total_health}")



