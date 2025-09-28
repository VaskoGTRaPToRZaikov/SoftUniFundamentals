fire_input = input().split("#")
water = int(input())

extinguished_cells = []
total_effort = 0
total_fire = 0

for data in fire_input:
    if "=" not in data:
        continue

    fire_type, value_string = data.split("=")
    fire_type = fire_type.strip()
    cell_value = int(value_string.strip())

    if (fire_type == "High" and 81 <= cell_value <= 125) \
            or (fire_type == "Medium" and 51 <= cell_value <= 80) \
            or (fire_type == "Low" and 1 <= cell_value <= 50):

        if water < cell_value:
            continue

        else:
            water -= cell_value
            effort = cell_value * 0.25
            total_effort += effort
            total_fire += cell_value
            extinguished_cells.append(cell_value)

    else:
        continue

print("Cells:")
for cells in extinguished_cells:
    print(f"- {cells}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")




