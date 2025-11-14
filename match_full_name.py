import re

names = input()

patter = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'

match = re.findall(patter, names)

print(' '.join(match))