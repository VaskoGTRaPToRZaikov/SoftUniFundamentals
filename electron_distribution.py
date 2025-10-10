number_of_electrons = int(input())

list_of_shells = []
shell_position = 1
while number_of_electrons:

    maximum_electrons_in_current_shel = 2 * shell_position ** 2

    if number_of_electrons >= maximum_electrons_in_current_shel:
        list_of_shells.append(maximum_electrons_in_current_shel)
        number_of_electrons -= maximum_electrons_in_current_shel

    else:
        list_of_shells.append(number_of_electrons)
        number_of_electrons = 0
    shell_position += 1

print(list_of_shells)