population = [int(number) for number in input().split(", ")]
minimum_wealth = int(input())

overall_wealth = sum(population)
required_wealth = len(population) * minimum_wealth

if overall_wealth < required_wealth:
    print("No equal distribution possible")
else:
    while min(population) < minimum_wealth:

        poorest_index = population.index(min(population))
        richest_index = population.index(max(population))

        needed_wealth = minimum_wealth - population[poorest_index]
        available_wealth = population[richest_index] - minimum_wealth

        transfer = min(needed_wealth, available_wealth)

        population[poorest_index] += transfer
        population[richest_index] -= transfer

    print(population)