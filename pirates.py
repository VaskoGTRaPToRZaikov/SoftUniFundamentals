def plunder(towns_info, some_town, some_peoples, some_gold):
    plundered_gold = min(some_gold, towns_info[some_town]["gold"])
    killed_citizens = min(some_peoples, towns_info[some_town]["population"])
    if some_gold >= towns_info[some_town]["gold"] or some_peoples >= towns_info[some_town]["population"]:
        del towns_info[some_town]
    else:
        towns_info[some_town]["gold"] -= some_gold
        towns_info[some_town]["population"] -= some_peoples
    return f"{some_town} plundered! {plundered_gold} gold stolen, {killed_citizens} citizens killed."

def prosper(towns_info, some_town, some_gold):
    if some_gold > 0:
        towns_info[some_town]["gold"] += some_gold
        total_gold = towns_info[some_town]["gold"]
        return f"{some_gold} gold added to the city treasury. {some_town} now has {total_gold} gold."
    return "Gold added cannot be a negative number!"

towns = {}

while True:
    town_info = input()

    if town_info == "Sail":
        break

    parts = town_info.split("||")
    town = parts[0]
    population = int(parts[1])
    gold = int(parts[2])

    if town not in towns:
        towns[town] = {"population": 0, "gold": 0}
    towns[town]["population"] += population
    towns[town]["gold"] += gold

while True:
    actions = input()

    if actions == "End":
        break

    elements = actions.split("=>")
    action = elements[0]

    if action == "Plunder":
        current_town = elements[1]
        peoples = int(elements[2])
        current_gold = int(elements[3])
        result = plunder(towns, current_town, peoples, current_gold)
        print(result)
        if current_town not in towns:
            print(f"{current_town} has been wiped off the map!")

    elif action == "Prosper":
        current_town = elements[1]
        current_gold = int(elements[2])
        result = prosper(towns, current_town, current_gold)
        print(result)
if not towns:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    count = len(towns)
    print(f"Ahoy, Captain! There are {count} wealthy settlements to go to:")
    for current_town, info in towns.items():
        people, gold = info.values()
        print(f"{current_town} -> Population: {people} citizens, Gold: {gold} kg")