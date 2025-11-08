text = input()

new_text = ""
strength = 0

for i in range(len(text)):
    if text[i] == ">":
        new_text += ">"
        strength += int(text[i + 1])

    elif strength > 0:
        strength -= 1

    else:
        new_text += text[i]

print(new_text)

