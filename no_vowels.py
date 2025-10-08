text = input()

without_vowels = [char for char in text if char.lower() not in ("a", "o", "u", "e", "i")]

print(''.join(without_vowels))