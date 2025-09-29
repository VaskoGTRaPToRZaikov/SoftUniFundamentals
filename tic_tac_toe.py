row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))

board = [row1, row2, row3]

winner1 = False
winner2 = False

for row in board:
    if all(cell == 1 for cell in row):
        winner1 = True
        break

if not winner1:
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == 1:
            winner1 = True
            break

if not winner1:
    if board[0][0] == board[1][1] == board[2][2] == 1:
        winner1 = True
    elif board[0][2] == board[1][1] == board[2][0] == 1:
        winner1 = True

for row in board:
    if all(cell == 2 for cell in row):
        winner2 = True
        break

if not winner2:
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == 2:
            winner2 = True
            break

if not winner2:
    if board[0][0] == board[1][1] == board[2][2] == 2:
        winner2 = True
    elif board[0][2] == board[1][1] == board[2][0] == 2:
        winner2 = True

if winner1:
    print("First player won")
elif winner2:
    print("Second player won")
else:
    print("Draw!")