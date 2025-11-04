number_of_dragons = int(input())
dragon_stats = {}
dragons_order = []


for _ in range(number_of_dragons):
    current_dragon = input().split()
    dragon_type, dragon_name, dragon_power, dragon_life, dragon_def = current_dragon

    dragon_damage = 45 if dragon_power == "null" else int(dragon_power)
    dragon_health = 45 if dragon_life == "null" else int(dragon_life)
    dragon_armor = 45 if dragon_def == "null" else int(dragon_def)

    if dragon_type not in dragons_order:
        dragons_order.append(dragon_type)

    if dragon_type not in dragon_stats:
        dragon_stats[dragon_type] = {}

    stats = {
        'damage': dragon_damage,
        'health': dragon_health,
        'armor': dragon_armor
    }
    dragon_stats[dragon_type][dragon_name] = stats

for dragon_type in dragons_order:
    type_of_dragon = dragon_stats[dragon_type]
    num_dragons = len(type_of_dragon)
    total_damage = sum(stats["damage"] for stats in type_of_dragon.values())
    total_health = sum(stats["health"] for stats in type_of_dragon.values())
    total_armor = sum(stats["armor"] for stats in type_of_dragon.values())

    average_damage = round(total_damage / num_dragons, 2)
    average_health = round(total_health / num_dragons, 2)
    average_armor = round(total_armor / num_dragons, 2)

    print(f"{dragon_type}::({average_damage}/{average_health}/{average_armor})")

    sorted_names = sorted(type_of_dragon.keys())

    for name in sorted_names:
        stats = type_of_dragon[name]
        print(f"-{name} -> damage: {stats['damage']}, health: {stats['health']}, armor: {stats['armor']}")