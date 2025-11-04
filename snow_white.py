dwarfs = {}

order_of_input = {}
counter_input = 0

while True:
    command = input()

    if command == "Once upon a time":
        break

    elements = command.split(" <:> ")
    name = elements[0]
    hat_color = elements[1]
    physics = int(elements[2])

    key = (name, hat_color)

    if key not in dwarfs:
        dwarfs[key] = physics
        order_of_input[key] = counter_input
        counter_input += 1

    elif physics > dwarfs[key]:
        dwarfs[key] = physics

hat_color_count = {}

for (name, hat_color), physics in dwarfs.items():
    hat_color_count[hat_color] = hat_color_count.get(hat_color, 0) + 1

dwarfs_list = []

for (name, hat_color), physics in dwarfs.items():
    color_count = hat_color_count[hat_color]
    input_order = order_of_input[(name, hat_color)]

    dwarfs_list.append({
        "name": name,
        "hat_color": hat_color,
        "physics": physics,
        "color_count": color_count,
        "input_order": input_order
    })

dwarfs_list.sort(key=lambda x: (
    -x["physics"],
    -x["color_count"],
    x["input_order"]
))

for dwarfs in dwarfs_list:
    print(f"({dwarfs['hat_color']}) {dwarfs['name']} <-> {dwarfs['physics']}")