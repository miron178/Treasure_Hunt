from random import randint

empty = '-'
bandit = 'b'  #makes symbols for bandits, chests and empty spaces used later in code
chest30 = 'C'
chest20 = 'c'
chest10 = '.'
player = 'X'

def random_space(board): #makes random space/place
    rows = len(board)
    cols = len(board[0])
    row = randint(0, rows -1)
    col = randint(0, cols -1)
    return (row, col)

def is_free (board, row, col): #part of cheking if space is empty
    return board[row][col] == empty

def find_free_space(board): #cheking if space is free
    found = False # if not free looks for another space
    while not found:
        (row,col) = random_space(board)
        found = is_free (board, row, col)
    return(row, col)

def add_one(board, what):
    (row, col) = find_free_space(board)
    board[row][col] = what

def add_bandits (board, num):
    for x in range(num):
        add_one(board, bandit)

def add_chests (board, num):
    for x in range(num):
        add_one(board, chest30)

def make_board(rows, cols, bandits, chests): #uses numbers from the 2nd to bottom line
    assert(bandits + chests <= rows * cols-1) #makes sure that there are not more bandits and chests than places on grid
    print ('making board %d rows by %d columns' % (rows, cols)) #%d is replaced by item in brackets after the % behind text
    board = [[empty for x in range(cols)] for y in range(rows)]
    board [rows-1][0] = player #stop from placing anything in the bottom left corner
    add_bandits(board, bandits)
    add_chests(board, chests)
    board [rows-1][0] = empty
    return board

def player_placement(board):
    row = len(board) - 1
    col = 0
    return (row,col)

def print_board(board,player_row,player_col,show):
    rows = len(board)
    cols = len(board[0])
    print ('printing board %d rows by %d columns' % (rows, cols))
    for row in range (rows):
        line=""
        for col in range (cols):
            if row == player_row and col == player_col:
                left = "["
                right = "]"
                mid = board[row][col]
            else:
                left = " "
                right = " "
                if show:
                    mid = board[row][col]
                else:
                    mid = empty
            line = line + left + mid + right
        print (line)

game_board = make_board(8,8,5,10) #FIRST TWO NUM = COL AND ROW LAST TWO NUM = BANDITS AND CHESTS
(player_row,player_col) = player_placement(game_board)
print_board(game_board,player_row,player_col,False)
