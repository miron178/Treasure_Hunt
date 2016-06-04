#import grid
from random import randint

#making board
board = []
for x in range(8):
    board.append((["◻"]) * 8)

def print_board (board):
    for row in board:
        print ((" ").join(row))

print("this is the board")

# make player

def row_7(board):
    return randint(0, len(board) - 1)
def col_0(board):
    return randint(0, len(board) - 1)

player_row = 7
player_col = 0
print ("")
board[player_row][player_col] = "X"

#make chests

def Make_Chest (chest):
    for row in chest:
        print ((" ").join(row))

def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board) - 1)


#insert chests

chest_row = random_row(board)
chest_col = random_col(board)

chest_row1 = random_row(board)
chest_col1 = random_col(board)

chest_row2 = random_row(board)
chest_col2 = random_col(board)

chest_row3 = random_row(board)
chest_col3 = random_col(board)

chest_row4 = random_row(board)
chest_col4 = random_col(board)

chest_row5 = random_row(board)
chest_col5 = random_col(board)

chest_row6 = random_row(board)
chest_col6 = random_col(board)

chest_row7 = random_row(board)
chest_col7 = random_col(board)

chest_row8 = random_row(board)
chest_col8 = random_col(board)

chest_row9 = random_row(board)
chest_col9 = random_col(board)

chest1=3
#repeat for all 10

chest_play = chest1 #plus the rest

board[chest_row][chest_col] = "0"

board[chest_row1][chest_col1] = "1"

board[chest_row2][chest_col2] = "2"

board[chest_row3][chest_col3] = "3"

board[chest_row4][chest_col4] = "4"

board[chest_row5][chest_col5] = "5"

board[chest_row6][chest_col6] = "6"

board[chest_row7][chest_col7] = "7"

board[chest_row8][chest_col8] = "8"

board[chest_row9][chest_col9] = "9"

print_board(board)

#Make coin counter

while chest_play > 0:
    print ("time to hunt treasure")
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess col: "))

    if player_row == chest_row and player_col == chest_col:
        print ("you landed on a treasure chest!")
        print ("you have " + str(coins) + "coins")
        print ("Treasure chest count is " +str(TC_count_1))
        print ("play: " +str(play))
        if coins == 100:
            print_board(board)
            print ("you win")

        chest_row = bandit_row
        chest_col = bandit_col
        board [bandit_col][bandit_row]="B"
        print("another one ")
        print_board(board)
        print ("you have been robbed")
        board[chest1_row][chest1_col]= "B"
        coins = 0
        print ("play: "+ str(chest_play))

    if guess_row == bandit_row and guess_col == bandit_col:
        print ("you have been robbed")
        board[chest1_row][chest1_col]= "B"
        coins = 0
        print ("you now have " + str(coins) + "coins")
        print_board(board)

    if play <=  0:
        break

#player moveing

#for turn in range(9001):
 #   print ("")
  #  print (("Turn"), turn + 1)
  #  guess_row = int(input("Guess Row: "))
  #  guess_col = int(input("Guess Col: "))

   # board[guess_row][guess_col] = "X"
   # print_board(board)
