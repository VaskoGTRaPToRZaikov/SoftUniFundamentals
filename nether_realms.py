import re

demons = input().split(",")
demons = [demon.strip() for demon in demons]

health_pattern = r"[^+\-*\/0-9.]"
damage_pattern = r"[+-]?\d+\.?\d*"
multiplier_pattern = r"[*\/]"
demons.sort()

for demon in demons:
    health_match = re.findall(health_pattern,demon)
    damage_match = re.findall(damage_pattern,demon)
    multipliers = re.findall(multiplier_pattern, demon)
    health = sum(ord(char) for char in health_match)
    damage = sum(float(num) for num in damage_match)
    if multipliers:
        characters = "".join(multipliers)
        for char in characters:
            if char == "*":
                damage *= 2
            elif char == "/":
                damage /= 2

    print(f"{demon} - {health} health, {damage:.2f} damage")
