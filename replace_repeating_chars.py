text = input()

new_text = ""

for i in range(len(text)):
    if not new_text or new_text[-1] != text[i]:
        new_text += text[i]

print(new_text)