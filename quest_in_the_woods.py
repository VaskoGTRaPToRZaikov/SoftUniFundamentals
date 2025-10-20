days_of_adventure = int(input())
number_of_participants = int(input())
groups_energy = float(input())
daily_person_water = float(input())
daily_person_food = float(input())

total_water = daily_person_water * days_of_adventure * number_of_participants
total_food = daily_person_food * days_of_adventure * number_of_participants

for day in range(1, days_of_adventure + 1):
    energy_loss = float(input())

    groups_energy -= energy_loss


    if groups_energy <= 0:
        print(f"You will run out of energy. You will be left with"
              f" {total_food:.2f} food and {total_water:.2f} water.")
        break

    if day % 2 == 0:
        groups_energy *= 1.05
        total_water *= 0.70

    if day % 3 == 0:
        groups_energy *= 1.10
        total_food -= total_food / number_of_participants

if groups_energy > 0:
    print(f"You are ready for the quest. You will be left with {groups_energy:.2f} energy!")

