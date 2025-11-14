import re

name_pattern = r"[A-Za-z]"
distance_pattern = r"\d"

participants = input().split(", ")
racers = {}

for player in participants:
    racers[player] = 0

while True:
    text = input()

    if text == "end of race":
        break

    name_characters = re.findall(name_pattern, text)
    name = "".join(name_characters)

    distance_digits = re.findall(distance_pattern, text)
    distance = sum(map(int, distance_digits))

    if name in racers:
        racers[name] += distance

sorted_player = sorted(racers.items(), key=lambda x: -x[1])
first_racer, second_racer, third_racer = sorted_player[0][0], sorted_player[1][0], sorted_player[2][0]

print(f"1st place: {first_racer}\n2nd place: {second_racer}\n3rd place: {third_racer}")
