phonebook = {}

while True:
    entry = input()

    if "-" in entry:
        info = entry.split("-")
        name, number = info[0], info[1]
        phonebook[name] = number


    else:
        number_of_searches = int(entry)
        break



for _ in range(number_of_searches):
    name = input()
    if name in phonebook.keys():
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")

