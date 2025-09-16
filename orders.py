numbers_of_orders = int(input())
price = 0
total_price = 0

for _ in range(numbers_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_per_day = int(input())

    if 0.01 <= price_per_capsule <= 100.00:

        if 1 <= days <= 31:

            if 1 <= capsule_per_day <= 2000:

                price = price_per_capsule * capsule_per_day * days

                print(f"The price for the coffee is: ${price:.2f}")

    total_price += price

print(f"Total: ${total_price:.2f}")

