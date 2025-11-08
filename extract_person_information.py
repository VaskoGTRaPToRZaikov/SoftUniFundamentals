def information(some_text):
    name_start_index, name_end_index = [text.index("@"), text.index("|")]
    age_start_index, age_end_index = [text.index("#"), text.index("*")]
    name = text[name_start_index + 1: name_end_index]
    age = text[age_start_index + 1: age_end_index]

    return f"{name} is {age} years old."

number_of_lines = int(input())

for _ in range(number_of_lines):
    text = input()

    print(information(text))