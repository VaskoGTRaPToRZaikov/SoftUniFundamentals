number_of_pieces = int(input())
pieces = {}

for _ in range(number_of_pieces):
    parts = input().split("|")
    piece = parts[0]
    composer = parts[1]
    key = parts[2]
    pieces[piece] = {"composer": composer, "key": key}

while True:
    command = input()

    if command == "Stop":
        break

    elements = command.split("|")
    action = elements[0]

    if action == "Add":
        piece = elements[1]
        composer = elements[2]
        key = elements[3]
        if piece in pieces.keys():
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == "Remove":
        piece = elements[1]
        if piece in pieces.keys():
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        piece = elements[1]
        new_key = elements[2]

        if piece in pieces.keys():
            pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, data in pieces.items():
    print(f"{piece} -> Composer: {data['composer']}, Key: {data['key']}")

