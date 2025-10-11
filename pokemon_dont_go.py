pokemon_distances = [int(digit) for digit in input().split()]
summed_value = 0

while pokemon_distances:
    index = int(input())

    if index < 0:
        removed_element = pokemon_distances.pop(0)
        pokemon_distances.insert(0, pokemon_distances[-1])

    elif index >= len(pokemon_distances):
        removed_element = pokemon_distances.pop(-1)
        pokemon_distances.append(pokemon_distances[0])

    else:
        removed_element = pokemon_distances.pop(index)

    for i in range(len(pokemon_distances)):
        if removed_element >= pokemon_distances[i]:
            pokemon_distances[i] += removed_element
        else:
            pokemon_distances[i] -= removed_element
    summed_value += removed_element

print(summed_value)