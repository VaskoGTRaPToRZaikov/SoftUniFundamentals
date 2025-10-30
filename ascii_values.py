list_or_characters = input().split(", ")

my_dict = {char: ord(char) for char in  list_or_characters}

print(my_dict)