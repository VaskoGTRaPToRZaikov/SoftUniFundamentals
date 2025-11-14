import re
orders = {}

pattern = r"%([A-Z][a-z]+)%[^|$%\.]*<(\w+)>[^|$%\.]*\|(\d+)\|[^|$%\.0-9]*(\d+\.?\d*)\$"

while True:
    order = input()
    if order == "end of shift":
        break

    match = re.search(pattern, order)
    if match:
        customer, product, count, price = match.groups()
        total_price = int(count) * float(price)

        if customer not in orders:
            orders[customer] = 0

        orders[customer] += total_price

        print(f"{customer}: {product} - {total_price:.2f}")

income = sum(orders.values())
print(f"Total income: {income:.2f}")
