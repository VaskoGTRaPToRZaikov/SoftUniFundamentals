def cast_spell(some_heroes, some_hero, mana_needed, spells_name):
    if some_heroes[some_hero]["MP"] >= mana_needed:
        some_heroes[some_hero]["MP"] -= mana_needed
        mp_left = some_heroes[some_hero]["MP"]
        return f"{some_hero} has successfully cast {spells_name} and now has {mp_left} MP!"
    return f"{some_hero} does not have enough MP to cast {spells_name}!"

def take_damage(some_heroes, some_hero, some_damage, some_attacker):
    some_heroes[some_hero]["HP"] -= some_damage
    if some_heroes[some_hero]["HP"] > 0:
        current_hp = some_heroes[some_hero]["HP"]
        return f"{some_hero} was hit for {some_damage} HP by {some_attacker} and now has {current_hp} HP left!"
    del some_heroes[some_hero]
    return f"{some_hero} has been killed by {some_attacker}!"

def recharge(some_heroes, some_hero, recharge_amount):
    current_mana = some_heroes[some_hero]["MP"]
    some_heroes[some_hero]["MP"] += recharge_amount
    if some_heroes[some_hero]["MP"] > 200:
        some_heroes[some_hero]["MP"] = 200
        recovered_mana = some_heroes[some_hero]["MP"] - current_mana
        return f"{some_hero} recharged for {recovered_mana} MP!"
    return f"{some_hero} recharged for {recharge_amount} MP!"

def healing(some_heroes, some_hero, heal_amount):
    current_health = some_heroes[some_hero]["HP"]
    some_heroes[some_hero]["HP"] += heal_amount
    if some_heroes[some_hero]["HP"] > 100:
        some_heroes[some_hero]["HP"] = 100
        healed_amount = some_heroes[some_hero]["HP"] - current_health
        return f"{some_hero} healed for {healed_amount} HP!"
    return f"{some_hero} healed for {heal_amount} HP!"


number_of_heroes = int(input())
heroes = {}

for _ in range(number_of_heroes):
    hero_info = input().split()
    hero = hero_info[0]
    health_points, mana_points = int(hero_info[1]), int(hero_info[2])
    heroes[hero] = {}
    heroes[hero] = {"HP": health_points, "MP": mana_points}

while True:
    command = input()

    if command == "End":
        break

    parts = command.split(" - ")
    action, hero_name = parts[0], parts[1]

    if action == "CastSpell":
        mp_needed = int(parts[2])
        spell_name = parts[3]
        result = cast_spell(heroes,hero_name, mp_needed, spell_name)
        print(result)

    elif action == "TakeDamage":
        damage = int(parts[2])
        attacker = parts[3]
        result = take_damage(heroes, hero_name, damage, attacker)
        print(result)

    elif action == "Recharge":
        recharge_mana = int(parts[2])
        result = recharge(heroes, hero_name, recharge_mana)
        print(result)

    elif action == "Heal":
        heal = int(parts[2])
        result = healing(heroes, hero_name, heal)
        print(result)

for member, stat in heroes.items():
    health, mana = stat.values()
    print(f"{member}\nHP: {health}\nMP: {mana}")