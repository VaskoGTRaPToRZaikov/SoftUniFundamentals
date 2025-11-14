def take_odd(some_password):
    new_text = ""
    for i in range(len(some_password)):
        if i % 2 != 0:
            new_text += some_password[i]
    return new_text

def cut(some_password, some_index, some_length):
    cut_substring = some_password[some_index:some_index + some_length]
    first_occurrence_index = some_password.index(cut_substring)
    some_password = some_password[:first_occurrence_index] + some_password[first_occurrence_index + some_length:]
    return some_password

password = input()

while True:
    command = input()

    if command == "Done":
        break

    parts = command.split()
    action = parts[0]

    if action == "TakeOdd":
        password = take_odd(password)
        print(password)

    elif action == "Cut":
        index = int(parts[1])
        length = int(parts[2])
        password = cut(password, index, length)
        print(password)

    elif action == "Substitute":
        substring = parts[1]
        substitute_char = parts[2]
        if substring in password:
            password = password.replace(substring, substitute_char)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")