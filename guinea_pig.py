quantity_food = float(input())
quantity_hay = float(input())
quantity_cover = float(input())
pig_weight = float(input())

is_enough = True

for day in range(1, 31):

    quantity_food -= 0.300

    if day % 2 == 0:
        quantity_hay -= quantity_food * 0.05

    if day % 3 == 0:
        quantity_cover -= pig_weight / 3

    if quantity_food <= 0 or quantity_hay <= 0 or quantity_cover <= 0:
        is_enough = False
        break

if is_enough:
    print(f"Everything is fine! Puppy is happy! Food:"
          f" {quantity_food:.2f}, Hay: {quantity_hay:.2f},"
          f" Cover: {quantity_cover:.2f}.")
else:
    print(f"Merry must go to the pet store!")
