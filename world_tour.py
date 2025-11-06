travel_stops = input()

while True:
    command = input()

    if command == "Travel":
        break

    parts = command.split(":")
    action = parts[0]

    if action == "Add Stop":
        index = int(parts[1])
        destination = parts[2]
        if 0 <= index <= len(travel_stops):
            travel_stops = travel_stops[:index] + destination + travel_stops[index:]


    elif action == "Remove Stop":
       start_index = int(parts[1])
       end_index = int(parts[2])

       if 0 <= start_index < len(travel_stops) and 0 <= end_index < len(travel_stops):
           travel_stops = travel_stops[:start_index] + travel_stops[end_index + 1:]


    elif action == "Switch":
        old_string = parts[1]
        new_string = parts[2]

        if old_string in travel_stops:
            travel_stops = travel_stops.replace(old_string, new_string)
    print(travel_stops)

print(f"Ready for world tour! Planned stops: {travel_stops}")