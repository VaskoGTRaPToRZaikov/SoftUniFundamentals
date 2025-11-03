products = {}

while True:
    command = input()

    if command == "buy":
        break

    product_information = command.split()
    name, price, quantity = product_information[0], float(product_information[1]), int(product_information[2])

    if name not in products:
        products[name] = {"price": price, "quantity": quantity}
    else:
        products[name]["price"] = price
        products[name]["quantity"] += quantity

for name, info in products.items():
    total_price = info["price"] * info["quantity"]
    print(f"{name} -> {total_price:.2f}")