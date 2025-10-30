elements = input().split()
stock = {}

for i in range(0, len(elements), 2):
    product = elements[i]
    quantity = elements[i + 1]
    stock[product] = int(quantity)

product_for_search = input().split()

for product in product_for_search:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

