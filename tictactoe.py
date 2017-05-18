from __future__ import print_function
from IPython.display import clear_output
def display_board(board):
    clear_output()
    #board = ['1','2','3','4','5','6','7','8','9']
    c = 2
    while (c >= 0):            
        print(" -"*6)
        print("| "+board[(3*c)]+" | "+board[(3*c+1)]+" | "+board[(3*c+2)]+" |")
        c -= 1
    print(" -"*6)

def player_input():
    player1 = ' '
    while not (player1 == "X" or player1 == "O"):
        player1 = raw_input("Player 1: Do you want to be O or X?").upper()
    
    if player1 == "X":
        return ("X", "O")
    else:
        return ("O", "X")
    
def place_input(board, player, pos):
    board[pos] = player

def check_win(board, player):
    check_row = False
    check_col = False
    check_diag = False
    x = 0
    ## if all symbols in one row or col or diagonal are the same
    while x < 3:
        ##check row
        check_row = (board[x*3] == board[x*3+1] == board[x*3+2] == player)
        ##check col
        check_col = (board[x] == board[3+x] == board[6+x] == player)
        if x == 1:
            check_diag = (board[2*x] == board[2*(x+1)]
                          == board[2*(x+2)] == player)
        if x == 0:
            check_diag = (board[4*x] == board[4*(x+1)]
                          == board[4*(x+2)] == player)
        
        if (check_row or check_col or check_diag):
            print("you are a winner!")
            return [player, True]
        else:
            x += 1
            
import random
def who_first():
    if random.randint(1,2) == 1:
        return 'Player2'
    else:
        return 'Player1'
    
def check_space(board, pos):
    
    return board[pos] == ' '

def check_board_full(board):
    for x in range(0,9):
        if check_space(board,x):
            return False
    return True

def player_choice(board):
    pos = ' '
    while (pos not in '1 2 3 4 5 6 7 8 9'.split() or
           not check_space(board, int(pos) - 1)):
        pos = raw_input('Enter your next position: (1-9)')   

    
    print("you chose position: "+ pos)        
    return int(pos)

def replay():
    choice = ' '
    while not (choice == 'y' or choice == 'n'):
        choice =  raw_input('Do you want to play again? Enter Y/N:').lower()
        
    return choice == 'y'

print("Welcome to Tic Tac Toe!")

#while True:
def play_tictactoe():
    #create the board
    score = [0,0,0]
    while True:
        board = [' ']*10
        player1, player2 = player_input()
        player = who_first()
        print (player + ' will play first!')
        game = True
        
        while game:
            if player == 'Player1':                
                display_board(board)
                print ('Your turn, Player1: ' + player1)
                pos = player_choice(board)
                place_input(board, player1, pos - 1)
                
                if check_win(board,player1):
                    display_board(board)
                    score[0] += 1
                    game = False
                else:
                    if check_board_full(board):
                        display_board(board)
                        print("The game is a draw!")
                        score[2] += 1
                        break
                    else:
                        player = 'Player2'
            else:
                # when Player 2 plays
                display_board(board)
                print ('Your turn, Player2: ' + player2)
                pos = player_choice(board)
                place_input(board, player2, pos - 1)
                if check_win(board,player2):
                    display_board(board)
                    score[1] += 1
                    game = False
                else:
                    if check_board_full(board):
                        display_board(board)                    
                        print("The game is a tie!")
                        score[2] += 1
                        break
                    else:
                        player = 'Player1'  
                        
        print(board)
        x = score[0]
        y = score[1]
        z = score[2]
        result = ('Player1 = '+ repr(x)+' : Player2 = '+repr(y)+
                  ' | Ties = '+repr(z))
        print(result)
        if not replay():
            break
            
play_tictactoe()            