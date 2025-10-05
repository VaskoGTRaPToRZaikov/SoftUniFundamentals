import math


def center_point(cord_x1, cord_y1, cord_x2, cord_y2):
    distance1 = cord_x1 ** 2 + cord_y1 ** 2
    distance2 = cord_x2 ** 2 + cord_y2 ** 2

    if distance1 <= distance2:
        return f"({math.floor(cord_x1)}, {math.floor(cord_y1)})"
    return f"({math.floor(cord_x2)}, {math.floor(cord_y2)})"

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

result = center_point(x1, y1, x2, y2)
print(result)