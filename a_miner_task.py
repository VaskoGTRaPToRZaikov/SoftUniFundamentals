command = input()
resources = {}
number_inputs = 1
while command != "stop":
    if number_inputs % 2 != 0:
        resource = command
        if command not in resources:
            resources[command] = 0
    elif number_inputs % 2 == 0:
        resources[resource] += int(command)
    number_inputs += 1
    command = input()

for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")
