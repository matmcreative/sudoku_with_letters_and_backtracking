# Sudoku (with letters, with number, and 25x25) | Python

## Table of Contents
* [Technologies](#Technologies)
* [Objective 1 - Sudoku 9x9](#Objective1)
* [Number Process](#Process1)
* [Objective 2 - Letter Sudoku 9x9](#Objective2)
* [Letter Process](#Process2)
* [Objective 3 - Giant Sudoku 25x25](#Objective3)
* [Number Process](#Process3)
* [Objective 4 - Giant Letter Sudoku](#Objective4)
* [Number Process](#Process4)
* [Troubleshooting](#Troubleshooting)

# Technologies
* Python

# Objective1 | Standard Sudoku (numbers, 9x9)
Create a Python script to solve standard 9x9 Sudoku puzzles.  Use the backtracking algorithm to find a solution to any solvable sudoku board.

# Process1 | Standard Sudoku (numbers, 9x9)
* Define the board layout
```
def print_board(brd):
    for i in range(len(brd)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(brd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(brd[i][j])
            else:
                print(str(brd[i][j]) + " ", end="")
```

* Create a script to pick empty positions on the puzzle board.
```
def find_empty(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0:
                return (i, j)  # row, col

    return None

```
* Create a script to see if board is valid
```
def valid(brd, num, pos):
    # Check row
    for i in range(len(brd[0])):
        if brd[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(brd)):
        if brd[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if brd[i][j] == num and (i,j) != pos:
                return False

    return True
```
* Create a script to try numbers 1-9 to see if they work and place number if it is valid. Backtrack if number does not work and reset space to zero.
```
def solve(brd):
    find = find_empty(brd)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(brd, i, (row, col)):
            brd[row][col] = i

            if solve(brd):
                return True

            brd[row][col] = 0

    return False
```
* Print board before solution, solve, print board after solution.
```
print_board(board)
solve(board)
print("_____________________________________________________________")
print_board(board)
```
# Objective2 | Letter Sudoku (letters, 9x9)
Create a Python script to solve 9x9 Sudoku puzzles using letters instead of numbers.  Use the backtracking algorithm to find a solution to any solvable sudoku board.

# Process2 | Letter Sudoku (letters, 9x9)
* Define the board layout
```
def print_board(brd):
    for i in range(len(brd)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(brd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(brd[i][j])
            else:
                print(str(brd[i][j]) + " ", end="")
```

* Create a script to pick empty positions on the puzzle board.
```
def find_empty(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0:
                return (i, j)  # row, col

    return None

```
* Create a script to see if board is valid
```
def valid(brd, num, pos):
    # Check row
    for i in range(len(brd[0])):
        if brd[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(brd)):
        if brd[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if brd[i][j] == num and (i,j) != pos:
                return False

    return True
```
* Create a script to try letters 'a-i' to see if they work and place letter if it is valid. Backtrack if letter does not work and reset space to zero. Repeat steps to fill all empty spaces.
```
def solve(brd):
    find = find_empty(brd)
    if not find:
        return True
    else:
        row, col = find

    for i in 'abcdefghi':
        if valid(brd, i, (row, col)):
            brd[row][col] = i

            if solve(brd):
                return True

            brd[row][col] = 0

    return False
```
* Print board before solution, solve, print board after solution.
```
print_board(board)
solve(board)
print("_____________________________________________________________")
print_board(board)
```
# Objective3 | Giant Sudoku (numbers, 25x25)
Create a Python script to solve standard 25x25 Sudoku puzzles.  Use the backtracking algorithm to find a solution to any solvable sudoku board.

# Process3 | Giant Sudoku (numbers, 25x25)
* Define the board layout
```
def print_board(brd):
    for i in range(len(brd)):
        if i % 5 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

        for j in range(len(brd[0])):
            if j % 5 == 0 and j != 0:
                print(" | ", end="")

            if j == 24:
                print(brd[i][j])
            else:
                print(str(brd[i][j]) + " ", end="")
```

* Create a script to pick empty positions on the puzzle board.
```
def find_empty(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0:
                return (i, j)  # row, col

    return None

```
* Create a script to see if board is valid
```
def valid(brd, num, pos):
    # Check row
    for i in range(len(brd[0])):
        if brd[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(brd)):
        if brd[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 5
    box_y = pos[0] // 5

    for i in range(box_y*5, box_y*5 + 5):
        for j in range(box_x*5, box_x*5 + 5):
            if brd[i][j] == num and (i,j) != pos:
                return False

    return True
```
* Create a script to try numbers 1-9 to see if they work and place number if it is valid. Backtrack if number does not work and reset space to zero.
```
def solve(brd):
    find = find_empty(brd)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,26):
        if valid(brd, i, (row, col)):
            brd[row][col] = i

            if solve(brd):
                return True

            brd[row][col] = 0

    return False
```
* Print board before solution, solve, print board after solution.
```
print_board(board)
solve(board)
print("_____________________________________________________________")
print_board(board)
```
# Objective4 | Giant Letter Sudoku (letters, 25x25)
Create a Python script to solve 25x25 Sudoku puzzles using letters instead of numbers.  Use the backtracking algorithm to find a solution to any solvable sudoku board.

# Process4 | Giant Letter Sudoku (letters, 25x25)
* Define the board layout
```
def print_board(brd):
    for i in range(len(brd)):
        if i % 5 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

        for j in range(len(brd[0])):
            if j % 5 == 0 and j != 0:
                print(" | ", end="")

            if j == 24:
                print(brd[i][j])
            else:
                print(str(brd[i][j]) + " ", end="")
```

* Create a script to pick empty positions on the puzzle board.
```
def find_empty(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0:
                return (i, j)  # row, col

    return None

```
* Create a script to see if board is valid
```
def valid(brd, num, pos):
    # Check row
    for i in range(len(brd[0])):
        if brd[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(brd)):
        if brd[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 5
    box_y = pos[0] // 5

    for i in range(box_y*5, box_y*5 + 5):
        for j in range(box_x*5, box_x*5 + 5):
            if brd[i][j] == num and (i,j) != pos:
                return False

    return True
```
* Create a script to try letters 'a-i' to see if they work and place letter if it is valid. Backtrack if letter does not work and reset space to zero. Repeat steps to fill all empty spaces.
```
def solve(brd):
    find = find_empty(brd)
    if not find:
        return True
    else:
        row, col = find

    for i in 'abcdefghijklmnopqrstuvwxy':
        if valid(brd, i, (row, col)):
            brd[row][col] = i

            if solve(brd):
                return True

            brd[row][col] = 0

    return False
```
* Print board before solution, solve, print board after solution.
```
print_board(board)
solve(board)
print("_____________________________________________________________")
print_board(board)
```
# Troubleshooting
* In Giant Sudoku, code runs properly, displays board and attempts to solve, but never finishes.  Tried checking numbers for errors, tried creating a new original board, error persists.
* In Giant Sudoku, challenge is to add leading 0's to single digit numbers in order for visual grid to line up prpoerly.  I know a solution is contained within the following code, but have not been anle to make it work when inserted.
```
for num in numbers:
  # Imagine the first num is 5 and the second is 12
  new_num = "0" + str(num)
  # Now the first num is "05" and the second is "012"
  new_num = new_num[-2:]
  # Now the first num is "05 and the second is "12"
```

