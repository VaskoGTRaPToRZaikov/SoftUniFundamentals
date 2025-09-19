text = input()

indices = [i for i in range(len(text)) if text[i].isupper()]

print(indices)