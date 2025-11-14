import re

pattern = r"((w{3})\.([a-z0-9\-]+)(\.[a-z]+)+)"
text = input()

while text:
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        matches = match.group(1)
        print(matches)
    text = input()
