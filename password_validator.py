def characters_long(word):
    if 6 <= len(word) <= 10:
        return True
    return "Password must be between 6 and 10 characters"

def only_letters_digits(word):
    if word.isalnum():
        return True
    return "Password must consist only of letters and digits"

def two_digits(word):
    digit_count = 0
    for symbol in word:
        if symbol.isdigit():
           digit_count += 1
    if digit_count >= 2:
        return True
    return "Password must have at least 2 digits"


def password_validator(word) -> list:
    is_valid = [characters_long(word), only_letters_digits(word), two_digits(word)]

    for index in range(len(is_valid) - 1, -1, -1):
        if isinstance(is_valid[index], bool):
            is_valid.pop(index)
    return is_valid

password = input()
password_is_not_valid = password_validator(password)
if password_is_not_valid:
    print("\n".join(password_is_not_valid))
else:
    print("Password is valid")