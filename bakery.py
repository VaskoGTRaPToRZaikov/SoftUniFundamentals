elements = input().split()

bakery = {}

for i in range(0, len(elements), 2):
    product = elements[i]
    quantity = elements[i + 1]
    bakery[product] = int(quantity)

print(bakery)
