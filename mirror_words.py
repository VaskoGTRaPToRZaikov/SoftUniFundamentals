import re

text = input()
words_pair = []
pattern = r"([@#])([A-z]{3,})\1{2}([A-z]{3,})\1"

matches = re.findall(pattern, text)
if matches:
    pairs = len(matches)


    for match in matches:
        reversed_word = match[1]
        reversed_word = reversed_word[::-1]
        if reversed_word == match[2]:
            words_pair.append(f"{match[1]} <=> {match[2]}")
    if words_pair:
        print(f"{pairs} word pairs found!")
        print(f"The mirror words are:\n{', '.join(words_pair)}")
    else:
        print(f"{pairs} word pairs found!")
        print("No mirror words!")

else:
    print("No word pairs found!")
    print("No mirror words!")