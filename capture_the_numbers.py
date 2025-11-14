import re

matches = []
pattern = r'\d+'
line = input()
while line:
    match = re.findall(pattern, line)
    matches += match

    line = input()

print(" ".join(matches))