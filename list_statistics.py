number_of_lines = int(input())

positive = []
negative = []

for _ in range(number_of_lines):
    number = int(input())
    if number >= 0:
        positive.append(number)

    elif number < 0:
        negative.append(number)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")