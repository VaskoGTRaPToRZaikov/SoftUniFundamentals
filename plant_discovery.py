number_of_plants = int(input())

plants_information = {}
rating_counter = {}

for _ in range(number_of_plants):
    information = input().split("<->")
    plant, rarity = information[0], int(information[1])
    plants_information[plant] = {"rarity": rarity}

while True:
    command = input()

    if command == "Exhibition":
        break

    elements = command.strip().split(":")
    action = elements[0]

    if action == "Rate":
        parts = elements[1].strip().split(" - ")
        current_plant, rating = parts[0], int(parts[1])

        if current_plant in plants_information.keys():
            if "rating" not in plants_information[current_plant].keys():
                plants_information[current_plant]["rating"] = 0
            plants_information[current_plant]["rating"] += rating
            if current_plant not in rating_counter.keys():
                rating_counter[current_plant] = 0
            rating_counter[current_plant] += 1
        else:
            print("error")

    elif action == "Update":
        parts = elements[1].strip().split(" - ")
        current_plant, new_rarity = parts[0], int(parts[1])
        if current_plant in plants_information.keys():
            plants_information[current_plant]["rarity"] = new_rarity
        else:
            print("error")

    elif action == "Reset":
        current_plant = elements[1].strip()
        if current_plant in plants_information.keys():
            if "rating" in plants_information[current_plant].keys():
                del plants_information[current_plant]["rating"]
                del rating_counter[current_plant]
        else:
            print("error")

print("Plants for the exhibition:")
for plant_name, info in plants_information.items():
    plant_rarity = info['rarity']
    if plant_name in rating_counter and rating_counter[plant_name] > 0:
        average_rating = info['rating'] / rating_counter[plant_name]
    else:
        average_rating = 0
    print(f"- {plant_name}; Rarity: {plant_rarity}; Rating: {average_rating:.2f}")