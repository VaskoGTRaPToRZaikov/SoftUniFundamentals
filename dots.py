def count_connected_dots(some_row, some_col, dot_type):
    if some_row < 0 or some_row >= rows\
        or some_col < 0 or some_col >= cols:
        return 0

    if visited[some_row][some_col] or board[some_row][some_col] != dot_type:
        return 0

    visited[some_row][some_col] = True

    count = 1

    count += count_connected_dots(some_row - 1, some_col, dot_type)
    count += count_connected_dots(some_row + 1, some_col, dot_type)
    count += count_connected_dots(some_row, some_col - 1, dot_type)
    count += count_connected_dots(some_row, some_col + 1, dot_type)

    return count

board_rows = int(input())

board = []
for _ in range(board_rows):
    row = input().split()
    board.append(row)

rows = len(board)
cols = len(board[0]) if rows > 0 else 0
visited = [[False] * cols for _ in range(rows)]

max_connected = 0

for i in range(rows):
    for j in range(cols):
        if not visited[i][j] and board[i][j] == ".":
            connected = count_connected_dots(i, j, ".")

            if connected > max_connected:
                max_connected = connected

print(max_connected)


