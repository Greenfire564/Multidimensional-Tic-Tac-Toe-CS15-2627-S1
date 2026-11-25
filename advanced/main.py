def display_grid(grid):
    for row in grid:
        print(row)


def determine_winner(grid):
    for row in grid:
        if row[0] == row[1] and row[1] == row[2] and row[0] !=" ":
            return row[0]

    for i in range(3):
        if grid[0][i] == grid[1][i] and grid[1][i] == grid[2][i] !=" ":
            return grid[0][i]

    if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] !=" ":
        return grid[0][0]

    if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] !=" ":
        return grid[0][2]

    return "Tie"

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
    ]



current_player = "X"
turns = 0

while turns < 9:
    print(f"Player {current_player}'s turn.")
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter col (0, 1, or 2): "))
            if row in [0, 1, 2] and col in [0, 1, 2]:
                if board[row][col] == " ":
                    break
                else:
                    print("Can not choose that spot")
            else:
                print("0-2 only")
        except ValueError:
            print("Enter a valid number.")
    board[row][col] = current_player

    display_grid(board)

    winner = determine_winner(board)
    if winner != "Tie":
        print(f"Player {winner} wins")
        break
    elif turns == 8:
        print("Tie")
        break

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    turns += 1