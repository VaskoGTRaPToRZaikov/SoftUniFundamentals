import re

phone_numbers = input()

patter = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'

match = re.findall(patter, phone_numbers)

print(", ".join(match))