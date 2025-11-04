stock_at_the_shop = {}
sold_quantities = 0

while True:
    command = input()

    if command == "Complete":
        break

    parts = command.split()
    action = parts[0]
    quantity = int(parts[1])
    food = parts[2]

    if action == "Receive":
        if quantity <= 0:
            continue
        if food not in stock_at_the_shop:
            stock_at_the_shop[food] = 0
        stock_at_the_shop[food] += quantity

    elif action == 'Sell':
        if food not in stock_at_the_shop.keys():
            print(f"You do not have any {food}.")

        else:
            if quantity > stock_at_the_shop[food]:
                quantity_for_sell = stock_at_the_shop[food]
                print(f"There aren't enough {food}. You sold the last {quantity_for_sell} of them.")
                del stock_at_the_shop[food]
                sold_quantities += quantity_for_sell
            else:
                print(f"You sold {quantity} {food}.")
                stock_at_the_shop[food] -= quantity
                sold_quantities += quantity
                if stock_at_the_shop[food] == 0:
                    del stock_at_the_shop[food]

for foods, quantities in stock_at_the_shop.items():
    print(f"{foods}: {quantities}")
print(f"All sold: {sold_quantities} goods")