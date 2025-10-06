neighborhoods = list(map(int, input().split("@")))
current_position = 0

while True:
    commands = input()

    if commands == "Love!":
        break

    jump_length = int(commands.split()[1])
    current_position += jump_length

    if current_position >= len(neighborhoods):
        current_position = 0

    neighborhoods[current_position] -= 2

    if neighborhoods[current_position] == 0:
        print(f"Place {current_position} has Valentine's day.")
    elif neighborhoods[current_position] < 0:
        print(f"Place {current_position} already had Valentine's day.")

print(f"Cupid's last position was {current_position}.")

failed_houses = sum(1 for hearts in neighborhoods if hearts > 0)

if failed_houses == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed_houses} places.")



