def decrypt_message(encrypted_line, some_key):
    """Decrypt a line by subtracting key values from ASCII codes"""
    decrypted_message = []
    key_length = len(some_key)

    for i, char in enumerate(encrypted_line):
        key_index = i % key_length
        decrypted_char = chr(ord(char) - some_key[key_index])
        decrypted_message.append(decrypted_char)

    return ''.join(decrypted_message)

def extract_treasure_info(decrypted_line):
    """Extract treasure type and coordinates from decrypted message."""
    treasure_start_index = decrypted_line.find('&')
    treasure_end_index = decrypted_line.find('&', treasure_start_index + 1)

    coordinates_start_index = decrypted_line.find('<')
    coordinates_end_index = decrypted_line.find('>')

    some_treasure_type = decrypted_line[treasure_start_index + 1: treasure_end_index]
    some_coordinates = decrypted_line[coordinates_start_index + 1: coordinates_end_index]

    return some_treasure_type, some_coordinates

key = [int(number) for number in input().split()]

while True:
    command = input()

    if command == "find":
        break

    decrypted = decrypt_message(command, key)

    treasure_type, coordinates = extract_treasure_info(decrypted)

    if treasure_type and coordinates:
        print(f"Found {treasure_type} at {coordinates}")