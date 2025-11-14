import re
number_of_messages = int(input())
messages = []
encrypted_pattern = r"[s,t,a,r]"

for _ in range(number_of_messages):
    code = input()
    match = re.findall(encrypted_pattern, code, re.IGNORECASE)
    count = len(match)

    decrypted_message = ""
    for char in code:
        decrypted_char = ord(char) - count
        decrypted_message += chr(decrypted_char)

    messages.append(decrypted_message)

decrypted_pattern = r"@([A-Za-z]+)[^@\-!:>]*:(\d+)[^@\-!:>]*\!([A,D])\![^@\-!:>]*\->(\d+)"
attacked_planets = []
destroyed_planets = []

for message in messages:
    match = re.search(decrypted_pattern, message)

    if match:
        planet = match.group(1)
        action = match.group(3)
        if action == "A":
            attacked_planets.append(planet)
        elif action == "D":
            destroyed_planets.append(planet)

attacked_planets.sort()
destroyed_planets.sort()

print(f"Attacked planets: {len(attacked_planets)}")
for planet_name in attacked_planets:
    print(f"-> {planet_name}")

print(f"Destroyed planets: {len(destroyed_planets)}")
for planet_name in destroyed_planets:
    print(f"-> {planet_name}")





