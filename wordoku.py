board = [
    ['d','a',0,0,0,'g',0,0,'e'],
    [0,0,'c','b',0,'i',0,0,'h'],
    [0,0,'h',0,'e','a','i','d',0],
    ['f','c','e',0,0,0,0,'g',0],
    [0,0,'b',0,0,0,'a',0,0],
    [0,'d',0,0,0,0,'h','e','b'],
    [0,'i','d','g','c',0,'f',0,0],
    ['c',0,0,'d',0,'f','b',0,0],
    ['h',0,0,'i',0,0,0,'c','d']
]

# Create function to solve board
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


# Create function to determine if placed numbers are valid
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


# Create function to print grid for puzzle board
def print_board(brd):
    for i in range(len(brd)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(brd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(brd[i][j])
            else:
                print(str(brd[i][j]) + " ", end="")


# Create function to determin if puzzle board contains empty values
def find_empty(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board)
solve(board)
print("___________________")
print_board(board)