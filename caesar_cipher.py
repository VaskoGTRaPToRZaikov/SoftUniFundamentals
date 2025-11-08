text = input()

encrypted_message = ""

for element in text:
    new_element = ord(element) + 3
    encrypted_message += chr(new_element)

print(encrypted_message)