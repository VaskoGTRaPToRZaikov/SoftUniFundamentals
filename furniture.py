import re

furniture_list = []
total_cost = 0
pattern = r">>([a-z]+)<<(\d+[\.]?\d+)!(\d+)"

while True:
    command = input()

    if command == "Purchase":
        break

    match = re.search(pattern, command, re.IGNORECASE)

    if match:
        furniture_name, price, quantity = match.groups()
        furniture_list.append(furniture_name)
        total_cost += float(price) * int(quantity)

print("Bought furniture:")

for furniture in furniture_list:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")