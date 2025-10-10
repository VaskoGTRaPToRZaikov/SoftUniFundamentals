secret_message = input().split()
decipher = []

for word in secret_message:

    digits = ''.join(char for char in word if char.isdigit())
    letters = [char for char in word if not char.isdigit()]

    first_char = chr(int(digits))
    letters[0], letters[-1] = letters[-1], letters[0]

    decipher.append(first_char + ''.join(letters))

print(" ".join(decipher))


