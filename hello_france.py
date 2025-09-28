item_collection = input().split("|")
budget = float(input())
selling_price_list = []
total_shopping_sum = 0
total_selling_sum = 0
ticket_price = 150

for items in item_collection:
    split_item = items.split("->")
    current_item, current_price = split_item[0], float(split_item[1])

    if budget < current_price:
        continue

    if (current_item == "Clothes" and current_price > 50)\
            or (current_item == "Shoes" and current_price > 35)\
            or (current_item == "Accessories" and current_price > 20.50):
        continue

    else:
            budget -= current_price
            selling_price = current_price * 1.40
            selling_price_list.append(f"{selling_price:.2f}")
            total_shopping_sum += current_price
            total_selling_sum += selling_price

print(" ".join(selling_price_list))
profit = total_selling_sum - total_shopping_sum
print(f"Profit: {profit:.2f}")

total_budget = budget + total_shopping_sum + profit

if total_budget >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")

