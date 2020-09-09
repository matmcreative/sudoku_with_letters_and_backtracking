board = [
    [0,'l','r','y','x',0,'n','i','u',0,'p',0,0,'a',0,'d','e',0,'c','j',0,0,'w',0,'o'],
    [0,'p',0,'e','w','b','h',0,0,'y','m','x',0,'i','g','a',0,'s','v',0,'n','q','u',0,'k'],
    ['v',0,0,'a',0,0,0,'f',0,'s','y','n','h','u','o',0,0,'w',0,'b',0,0,'c',0,0],
    [0,'n','d',0,0,0,0,'j','p',0,'q',0,'e',0,'c','x',0,'g',0,'k','t','m','l','y','b'],
    ['m',0,'j',0,0,'k','t','g','e','c','l',0,'d','w',0,0,'i','h','r',0,0,'s',0,0,0],
    ['l','t','y','x',0,0,0,'v',0,'k','e','s','w','b',0,0,'g','f',0,0,'m',0,0,0,0],
    ['p','r',0,0,'v','j','y',0,0,0,'t',0,'x',0,0,'e','s',0,'o',0,'q','u','f','k','a'],
    ['u',0,'a',0,0,'x',0,'m','s','d','g',0,'l','o',0,'p','h','q','n',0,'e','c',0,0,0],
    [0,'s',0,'h','n','o','f',0,'a','w',0,0,'y','v','u',0,'m','c','k',0,0,'l','r','b','j'],
    ['g',0,0,'o','q',0,'e',0,0,0,0,'d',0,0,'f','i',0,'r','l',0,0,'v',0,'p','n'],
    [0,0,'w','v','g','t','c','q',0,'h',0,'i','b',0,'l',0,'f',0,0,'u',0,'x','o','r',0],
    ['f','i',0,0,'p',0,0,'l','d','n','h',0,0,'m','r','s','v',0,0,0,0,'a',0,'q','t'],
    ['j','a','o','b','u',0,'m','s',0,0,0,0,'k','q','e',0,0,0,0,'t',0,'f','p','h',0],
    ['t','e',0,'m','d','r','w',0,'o',0,0,'u','c','j',0,0,0,'k','x',0,0,0,'b',0,0],
    ['s','k',0,0,0,'f','u',0,0,'g','d','a',0,0,0,'h',0,'n','y','p','v','i',0,'w',0],
    [0,'w',0,'l',0,'u','q',0,0,0,'x',0,'p',0,'s','b',0,'y','t',0,'f','o','n',0,'d'],
    [0,0,'b',0,0,'l',0,0,0,'i','a',0,0,0,'h',0,0,'d','e',0,0,0,'q','g',0],
    [0,0,'t',0,'k','c','p',0,'x',0,0,0,'v','e','n','q',0,'a',0,'w','i','r',0,0,'l'],
    ['e','d',0,'u','h',0,0,'o',0,'j',0,0,0,'y', 0,'f','k',0,0,0,'x',0,0,'m','c'],
    ['o','q',0,'s','f','m',0,'b','n',0,'w','k',0,'t',0,'r',0,0,0,'h','y','p',0,'j','v'],
    [0,'b','s',0,0,'q','a','h',0,0,0,0,'r',0,'x','j',0,0,'g','c',0,0,0,'v','i'],
    [0,'c','p',0,0,0,'k','y','r','v',0,'m',0,'h',0,'n','a',0,'s','l',0,'j','d','u',0],
    ['k','v',0,'t',0,'p',0,0,'i',0,'u',0,0,0,'y','o',0,'e','w',0,0,'h','g','c','f'],
    [0,0,'g','d','r',0,0,'w','j','o','b','p','t',0,'q',0,'x','u','m',0,'k','n',0,'a',0],
    ['q','o',0,0,'m','s',0,0,0,'t','v',0,'f','d',0,0,0,'i',0,0,'p','w','e',0,'x']
]

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


def find_empty(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board)
solve(board)
print("_____________________________________________________________")
print_board(board)