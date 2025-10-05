import math


def distance_from_center(x, y):
    return x ** 2 + y ** 2

def line_length(cord_x1, cord_y1, cord_x2, cord_y2):
    return (cord_x2 - cord_x1) ** 2 + (cord_y2 - cord_y1) ** 2

def longer_line(cord_x1, cord_y1, cord_x2, cord_y2, cord_x3, cord_y3, cord_x4, cord_y4):
    length1 = line_length(cord_x1, cord_y1, cord_x2, cord_y2)
    length2 = line_length(cord_x3, cord_y3, cord_x4, cord_y4)

    if length1 >= length2:

        if distance_from_center(cord_x1,cord_y1) <= distance_from_center(cord_x2, cord_y2):
            return f"({math.floor(cord_x1)}, {math.floor(cord_y1)})({math.floor(cord_x2)}, {math.floor(cord_y2)})"
        return f"({math.floor(cord_x2)}, {math.floor(cord_y2)})({math.floor(cord_x1)}, {math.floor(cord_y1)})"

    else:
        if distance_from_center(cord_x3, cord_y3) <= distance_from_center(cord_x4, cord_y4):
            return f"({math.floor(cord_x3)}, {math.floor(cord_y3)})({math.floor(cord_x4)}, {math.floor(cord_y4)})"
        return f"({math.floor(cord_x4)}, {math.floor(cord_y4)})({math.floor(cord_x3)}, {math.floor(cord_y3)})"

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

result = longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
print(result)