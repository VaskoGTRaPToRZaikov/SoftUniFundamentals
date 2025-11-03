number_of_commands = int(input())
parking_validations = {}

for _ in range(number_of_commands):
    commands = input().split()
    command = commands[0]
    name = commands[1]


    if command == "register":
        license_number = commands[2]

        if name not in parking_validations:
            parking_validations[name] = license_number
            print(f"{name} registered {license_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_number}")

    elif command == 'unregister':

        if name not in parking_validations:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del parking_validations[name]

for username, plate_number in parking_validations.items():
    print(f"{username} => {plate_number}")