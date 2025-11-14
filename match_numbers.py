import re

numbers = input()

patter = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

matches = re.finditer(patter, numbers)

for match in matches:
    print(match.group(), end=" ")