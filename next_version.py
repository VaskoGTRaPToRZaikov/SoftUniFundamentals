version = input().split(".")

version_as_integer = int("".join(version))
version_as_integer += 1

current_version = str(version_as_integer)

print(".".join(current_version))
