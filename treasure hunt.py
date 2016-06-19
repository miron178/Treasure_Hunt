from random import randint

empty = '-'
bandit = 'b'  #makes symbols for bandits, chests and empty spaces used later in code
chest30 = 'C'
chest20 = 'c'
chest10 = '.'
player = 'X'

coins = 0
win_coins = 100

show = True

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
        global coins
        coins += 30

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

def board_size(board):
    rows = len(board)
    cols = len(board[0])
    return (rows,cols)

def print_board(board,player_row,player_col,show):
    (rows,cols) = board_size(board)
    #print ('printing board %d rows by %d columns, %d coins' % (rows, cols, coins))
    print()
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

def enter(prompt,min,max):
    correct = False
    while not correct:
        s = input(prompt)

        try:
            value = int(s)
            correct = (value >= min) and (value <= max)
        except ValueError:
            pass

        if not correct:
            print ("value '%s' is incorrect" % s)
    return value

def ask_for_position(rows,cols):
    row = enter("enter row between 0 and %d: " % (rows -1), 0, rows -1)
    col = enter("enter col between 0 and %d: " % (cols -1), 0, cols -1)
    return (row,col)

def visit(board,row,col,player_coins):
    global coins
    if board[row][col] == chest30:
        board[row][col] = chest20
        coins -= 10
        player_coins += 10
        print("You found a chest with 30 coins and took 10!")
    elif board[row][col] == chest20:
        board[row][col] = chest10
        coins -= 10
        player_coins += 10
        print("You found a chest with 20 coins and took 10!")
    elif board[row][col] == chest10:
        board[row][col] = bandit
        coins -= 10
        player_coins += 10
        print("You found a chest with 10 coins and took 10!")
    elif board[row][col] == bandit:
        player_coins = 0
        print("You have been robbed!!!")
    else:
        print("Nothing to see here, move along.")
    print("You have %d coins now, %d coins are in the chests" % (player_coins, coins))
    return player_coins

game_board = make_board(8,8,5,10) #FIRST TWO NUM = COL AND ROW LAST TWO NUM = BANDITS AND CHESTS
(player_row,player_col) = player_placement(game_board)
print_board(game_board,player_row,player_col,show)

player_coins = 0
keep_playing = True
won = False
while keep_playing:
    (player_row,player_col) = ask_for_position(*board_size(game_board))
    player_coins = visit(game_board,player_row,player_col,player_coins)
    print_board(game_board,player_row,player_col,show)
    if player_coins >= win_coins:
        keep_playing = False
        won = True
    if coins  + player_coins < win_coins:
        keep_playing = False
        won = False

if won:
    print ("You Win")
else:
    print("You Lose")
print ("GAME OVER!!!")
