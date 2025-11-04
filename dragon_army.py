number_of_dragons = int(input())
dragon_stats = {}
dragons_order = []


for _ in range(number_of_dragons):
    current_dragon = input().split()
    dragon_type, dragon_name, dragon_power, dragon_life, dragon_def = current_dragon

    dragon_damage = 45 if dragon_power == "null" else int(dragon_power)
    dragon_health = 250 if dragon_life == "null" else int(dragon_life)
    dragon_armor = 10 if dragon_def == "null" else int(dragon_def)

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

    average_damage = total_damage / num_dragons
    average_health = total_health / num_dragons
    average_armor = total_armor / num_dragons

    print(f"{dragon_type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")

    sorted_names = sorted(type_of_dragon.keys())

    for name in sorted_names:
        stats = type_of_dragon[name]
        print(f"-{name} -> damage: {stats['damage']}, health: {stats['health']}, armor: {stats['armor']}")
