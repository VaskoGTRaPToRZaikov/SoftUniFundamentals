budget = float(input())
kg_flour_price = float(input())
eggs_pack_price = kg_flour_price * 0.75
liter_milk_price = kg_flour_price * 1.25

price_per_bread = kg_flour_price + eggs_pack_price + (liter_milk_price / 4)

bread_count = 0
colored_eggs = 0


while budget > price_per_bread:

    bread_count += 1
    colored_eggs += 3

    if bread_count % 3 == 0:
        colored_eggs -= (bread_count - 2)

    budget -= price_per_bread

money_left = budget

print(f"You made {bread_count} loaves of Easter bread! "
      f"Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")