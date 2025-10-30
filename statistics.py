stocks = {}

while True:
    products = input().split(": ")

    if products[0] == "statistics":
        print(f"Products in stock:")
        break

    product = products[0]
    quantity = int(products[1])
    if product not in stocks:
        stocks[product] = 0
    stocks[product] += quantity

total_products = len(stocks.keys())
total_quantity = sum(stocks.values())

for product, quantity in stocks.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")