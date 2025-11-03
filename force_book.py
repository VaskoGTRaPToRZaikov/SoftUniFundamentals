force_book = {}

while True:
    command = input()

    if command == "Lumpawaroo":
        break

    if " | " in command:
        force_side, force_user = command.split(" | ")
        force_user_is_part_of_the_force = False
        for list_with_force_users in force_book.values():
            if force_user in list_with_force_users:
                force_user_is_part_of_the_force = True
                break
        if not force_user_is_part_of_the_force:
            if force_side not in force_book:
                force_book[force_side] = []
            force_book[force_side].append(force_user)

    elif " -> " in command:
        force_user, force_side = command.split(" -> ")
        for list_with_force_users in force_book.values():
            if force_user in list_with_force_users:
                list_with_force_users.remove(force_user)
                break

        if force_side not in force_book:
            force_book[force_side] = []
        force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for force, members in force_book.items():
    if len(members) > 0:
        print(f"Side: {force}, Members: {len(members)}")
        for user in members:
            print(f"! {user}")