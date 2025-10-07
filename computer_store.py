total_price_without_taxes = 0
total_price = 0
taxes_amount = 0

invalid_order = False

while True:
    command = input()

    if command == "regular" or command == "special":
        taxes_amount = total_price_without_taxes * 0.20
        total_price = total_price_without_taxes + taxes_amount
        if command == "special":
            total_price *= 0.90

        if total_price == 0:
            invalid_order = True
            break

        print("Congratulations you've just bought a new computer!\n"
              f"Price without taxes: {total_price_without_taxes:.2f}$\n"
              f"Taxes: {taxes_amount:.2f}$\n"
              "-----------\n"
              f"Total price: {total_price:.2f}$")
        break

    price = float(command)

    if price <= 0:
        print("Invalid price!")
        continue
    else:
        total_price_without_taxes += price

if invalid_order:
    print("Invalid order!")

