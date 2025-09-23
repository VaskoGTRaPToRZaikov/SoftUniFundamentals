key_steps = int(input())
number_of_letters = int(input())

secret_word = ""

for i in range(number_of_letters):
    letter = input()
    secret_word += chr(ord(letter) + key_steps)

print(secret_word)
