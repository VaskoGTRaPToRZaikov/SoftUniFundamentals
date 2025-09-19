coffee_count = 0
events_count = 0

while True:
    events = input()

    if events == "END":
        if coffee_count > 5:
            print("You need extra sleep")
        else:
            print(coffee_count)
        break

    if events.lower() == "coding" or events.lower() == "dog" or \
            events.lower() == "cat" or events.lower() == "movie":

        if events == events.lower():
            coffee_count += 1

        elif events == events.upper():
            coffee_count += 2





