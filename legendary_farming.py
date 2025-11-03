farming_dictionary = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

legendary_item = ""
won_a_legendary_item = False

while not won_a_legendary_item:
    materials = input().split()
    for i in range(0, len(materials), 2):
        quantity = int(materials[i])
        material = materials[i + 1].lower()

        if material == "shards":
            farming_dictionary["shards"] += quantity
            if farming_dictionary["shards"] >= 250:
                legendary_item = "Shadowmourne"
                won_a_legendary_item = True
                farming_dictionary["shards"] -= 250
                break
        elif material == "fragments":
            farming_dictionary["fragments"] += quantity
            if farming_dictionary["fragments"] >= 250:
                legendary_item = "Valanyr"
                won_a_legendary_item = True
                farming_dictionary["fragments"] -= 250
                break
        elif material == "motes":
            farming_dictionary["motes"] += quantity
            if farming_dictionary["motes"] >= 250:
                legendary_item = "Dragonwrath"
                won_a_legendary_item = True
                farming_dictionary["motes"] -= 250
                break
        else:
            if material in farming_dictionary:
                farming_dictionary[material] += quantity
            else:
                farming_dictionary[material] = quantity

if won_a_legendary_item:
    print(f"{legendary_item} obtained!")
    for key, value in farming_dictionary.items():
        print (f"{key}: {value}")



