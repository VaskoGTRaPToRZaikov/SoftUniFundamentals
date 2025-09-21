number_of_snowballs = int(input())
max_value = 0
max_weight = 0
max_speed = 0
max_quality = 0

for snowball in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_speed = int(input())
    snowball_quality = int(input())

    snowball_score = (snowball_weight // snowball_speed) ** snowball_quality

    if max_value < snowball_score:
        max_value = snowball_score
        max_weight = snowball_weight
        max_speed = snowball_speed
        max_quality = snowball_quality

print(f"{max_weight} : {max_speed} = {max_value} ({max_quality})")