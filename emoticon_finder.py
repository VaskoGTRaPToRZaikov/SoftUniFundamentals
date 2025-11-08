text = input()

for i in range(len(text)):
    if text[i] == ":" and (i + 1) < len(text):
        print(f":{text[i + 1]}")
