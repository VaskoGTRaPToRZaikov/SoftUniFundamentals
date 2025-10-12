def find_path(maze, visited, row, col, moves):
    rows = len(maze)
    cols = len(maze[0]) if rows > 0 else 0

    if row < 0 or row >= rows or col < 0 or col >= cols:
        return moves

    if maze[row][col] == "#" or visited[row][col]:
        return -1

    visited[row][col] = True

    max_moves = -1

    result = find_path(maze, visited, row - 1, col, moves + 1)
    if result > max_moves:
        max_moves = result

    result = find_path(maze, visited, row + 1, col, moves + 1)
    if result > max_moves:
        max_moves = result

    result = find_path(maze, visited, row, col - 1, moves + 1)
    if result > max_moves:
        max_moves = result

    result = find_path(maze, visited, row, col + 1, moves + 1)
    if result > max_moves:
        max_moves = result

    visited[row][col] = False

    return max_moves

how_many_rows = int(input())
maze_map = []
kate_row = -1
kate_col = -1

for i in range(how_many_rows):
    row_maze = input()
    maze_map.append(row_maze)

    if "k" in row_maze:
        kate_row = i
        kate_col = row_maze.index("k")

rows_maze = len(maze_map)
cols_maze = len(maze_map[0]) if rows_maze > 0 else 0
visited_cells = [[False] * cols_maze for _ in range(rows_maze)]

number_moves = find_path(maze_map, visited_cells, kate_row, kate_col, 0)

if number_moves == -1:
    print("Kate cannot get out")
else:
    print(f"Kate got out in {number_moves} moves")

