import re

text = input()

pattern = r"([=\/])([A-Z][A-Za-z]{2,})\1"

matches = re.findall(pattern, text)

if matches:
    destinations = [match[1] for match in matches]
    travel_points = sum(len(word) for word in destinations)

    print(f'Destinations: {", ".join(destinations)}')
    print(f"Travel Points: {travel_points}")
else:
    print(f'Destinations: ')
    print(f"Travel Points: 0")