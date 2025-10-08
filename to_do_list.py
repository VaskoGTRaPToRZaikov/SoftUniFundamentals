notes = [0] * 10

while True:
    command = input()

    if command == "End":
        break

    tokens = command.split("-")
    index = int(tokens[0]) - 1
    note = tokens[1]

    notes.pop(index)
    notes.insert(index, note)

result = [part for part in notes if part != 0]
print(result)
