number_of_lines = int(input())

brackets = ""

for i in range(number_of_lines):
    random_string = input()

    if random_string == "(" or random_string == ")":
        brackets += random_string

if brackets == "()" * (len(brackets) // 2):
    print("BALANCED")

else:
    print("UNBALANCED")

