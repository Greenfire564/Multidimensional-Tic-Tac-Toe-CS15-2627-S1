def display_grid(grid):
    print(grid[0])
    for row in grid:
        print(row)


def determine_winner(grid):
    for row in grid:
        if row[0] == row[1] and row[1] == row[2]:
            return row[0]

    for i in range(3):
        if grid[0][i] == grid[1][i] and grid[1][i] == grid[2][i]:
            return grid[0][i]

    if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
        return grid[0][0]

    if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]:
        return grid[0][2]

    return "Tie"

grid_1 = [
    ["X", "X", "X"],
    ["O", "O", "X"],
    ["O", "X", "O"]
]

grid_2 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "O", "X"]
]

grid_3 = [
    ["X", "O", "O"],
    ["O", "X", "X"],
    ["O", "X", "X"]
]

grid_4 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "X", "X"]
]

print(grid_1)
print(" ")
print(determine_winner(grid_1))
print(" ")
print(grid_2)
print(" ")
print(determine_winner(grid_2))
print(" ")
print(grid_3)
print(" ")
print(determine_winner(grid_3))
print(" ")
print(grid_4)
print(" ")
print(determine_winner(grid_4))






