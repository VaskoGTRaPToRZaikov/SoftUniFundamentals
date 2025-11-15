import re

text = input()

pattern = r"([#|])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1([0-9]{1,4}|10000)\1"
days_left = 0

matches = re.findall(pattern, text)

if matches:
    match = matches[0][3]

    total_calories = sum(int(match[3]) for match in matches)
    days_left = total_calories // 2000
    print(f"You have food to last you for: {days_left} days!")

    for match in matches:
        item_name = match[1]
        expiration_date = match[2]
        calories = match[3]
        print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")
else:
    print(f"You have food to last you for: {days_left} days!")