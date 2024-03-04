import random
import os.path
import json
random.seed()

def draw_board(board):
    for row in board:
        print(" | ".join(row))
        print("___" * len(row))
    pass

def welcome(board):
    print("Welcome to the \"Unbeatable Noughts and Crossses\" ")
    draw_board(board)
    pass


def initialise_board(board):
    for i in range(3):
        for j in range(3):
            board[i][j]= ' '
    return board

    
def get_player_move(board):
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the Column (0, 1, or 2): "))

            if row not in range(3) or col not in range(3) or board[row][col] != ' ':
                raise ValueError("Space not available in the board")
            break  
        except ValueError as e:
            print("Error: ", e)
    return row,col

def choose_computer_move(board):
    while True:
        row = random.randint(0,2)
        col = random.randint(0,2)
        if board[row][col] == ' ':
            break
    return row,col

def check_for_win(board, mark):
    #to check the horizonatal values
   for i in range(3):
       if (board[i][0] ==board[i][1] ==board[i][2] == mark) or \
       (board[0][i] ==board[1][i] ==board[2][i] == mark):
        return True
    
    # to check the diagonal values
       if (board[0][0] ==board[1][1] ==board[2][2] == mark) or \
       (board[0][2] ==board[1][1] ==board[2][0] == mark):
        return True
   
   return False

def check_for_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True
        
def play_game(board):

    initialise_board(board)
    draw_board(board)

    # then in a loop, get the player move, update and draw the board
    while True:
        row,col = get_player_move(board)  
        board[row][col] = "X"
    
        if (check_for_win(board,"X")) == True:
            draw_board(board)
            print("\nCongratulations! You've won!!")
            return 1    #  return 1 for the score

        if check_for_draw ==  True:
            print("\nIt's a draw.")
            draw_board(board)
            return 0    # if drawn, return 0 for the score 
        
        comp_row,comp_col = choose_computer_move(board)
        board[comp_row][comp_col] = "O"

        draw_board(board)

        if (check_for_win(board,"O")) == True:
            draw_board(board)
            return -1    

        print(check_for_draw(board))
        if  check_for_draw(board) == True:
            draw_board(board)
            return 0                   

def menu():
    
    print("1- Play the game ")
    print("2- Save scores in 'leaderboard.txt' ")
    print("3- Load and display the scores from the 'leaderboard.txt' ")
    print('q- Quit ')
    choice = input("Enter your choice : ")
    return choice

def load_scores():

    if os.path.exists('leaderboard.txt'):
        with open('leaderboard.txt','r') as f:
            leaders = json.load(f)
        return leaders
    else:
        leaders = {}
    
def save_score(score):
    try:
        player_name = input("Enter your name: ") 
        scores = load_scores()
        scores[player_name] = score
        with open('leaderboard.txt','w') as f:
            json.dump(scores,f)

    except Exception:
        print("Score could not be saved.")

def display_leaderboard(leaders):
    print("Leaderboard : ")
    for name,score in leaders.items():
        print(f"{name} : {score}")



