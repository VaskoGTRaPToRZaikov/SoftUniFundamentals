sequence_of_integers = list(map(int, input().split()))

average_value = sum(sequence_of_integers) / len(sequence_of_integers)

if any(number > average_value for number in sequence_of_integers):

    greater_than_average = [number for number in sequence_of_integers if number > average_value]

    greater_than_average = sorted(greater_than_average, reverse=True)
    
    print(" ".join(map(str, greater_than_average[:5])))

else:
    print("No")