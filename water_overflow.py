tank_capacity = 255
number_of_lines = int(input())
liters_in_the_tank = 0

for _ in range(number_of_lines):
    liters_of_water = int(input())

    if tank_capacity < liters_of_water:
        print("Insufficient capacity!")
        continue

    else:
        tank_capacity -= liters_of_water
        liters_in_the_tank += liters_of_water

print(liters_in_the_tank)