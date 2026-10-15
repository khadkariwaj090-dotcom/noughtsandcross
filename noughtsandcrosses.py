import random
import os.path
import json
random.seed()

def draw_board(board):
    '''This funstion provides a layout to our game
        parameter: board from the play_games
        return: nothing
    '''
    print("-" * 13)
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-" * 13)
    

def welcome(board):
    '''This is the welcome message for user'''
    print('Welcome to the "Unbeatable Noughtes and Crosses" games')
    print("The board layout is shown below:")
    draw_board(board)
    print("When prompted, enter the number corresponding to the square you want.")
    

def initialise_board(board):
    '''above function basically resets the layout everytime
    user chooses to play
    returns: board'''
    count = 1 
    for r in range(3): 
        for c in range(3): 
            board[r][c] = str(count)
            count += 1
    return board
    
def get_player_move(board):
    '''This part handles the user input
    also checks the if the user input is valid or not
    returns: row and column'''
    while True:
        try:
            move = int(input("Choose your square 1-9"))
            if move < 1 or move > 9:
                raise ValueError
            row=(move-1)//3
            col=(move-1)%3
        
            if board[row][col] not in("X","O"):
                return row, col
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

def choose_computer_move(board):
    
    '''This part handles the computer input
    appends a tuple into a list
    randomly input is suffled and
    return: row and column'''
    free_cells = [] 

    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['X', 'O']:
                free_cells.append((r, c))

    row, col = random.choice(free_cells)
    return row, col


def check_for_win(board, mark):
    '''this function basically checks the entire 
    possibilities to win the game
    returns: either true or false'''
    #horizontal check
    for row in range(3):
        if all(board[row][column]==mark for column in range(3)):
            return True
        if all(board[column][row]==mark for column in range(3)):
            return True
    #diagonal check
    if all(board[row][row]==mark for row in range(3)):
        return True
    if all(board[row][2-row]==mark for row in range(3)): 
        return True
    return False

def check_for_draw(board):
    '''this function checks for draw
    it check each row and column and if 
    they are filled with X and O it returns true
    else false'''
    for row in range(3):
        for column in range(3):
            if board[row][column] not in ['X','O']:
                return False
    return True
        
def play_game(board):
    '''this is where the game logic is controlled
    and helps run in sync'''
    initialise_board(board)
    draw_board(board)

    while True:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)

        if check_for_win(board, 'X'):
            print("You win!")
            return 1

        if check_for_draw(board):
            print("It's a draw!")
            return 0

        
        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        print("Computer move:")
        draw_board(board)

        if check_for_win(board, 'O'):
            print("Computer wins!")
            return -1

        if check_for_draw(board):
            print("It's a draw!")
            return 0

                    
                
def menu():
    '''menu card of the game'''
    print("Enter one of the following opyions:")
    print("\n1 - Play game")
    print("2 - Save score")
    print("3 - Load leaderboard")
    print("q - Quit")

    choice = input("1,2,3 or q? ")
    return choice

def load_scores():
    '''This function checks if the leaderboard
    file is present or not if not 
    returns: empty dictionary
    it also reads the content in text format 
    returns: json into python dictionary'''
    if not os.path.exists("leaderboard.txt"):
        return {}

    with open("leaderboard.txt", "r") as file:
        leaders= json.load(file)
        return leaders

    
def save_score(score):
    '''This function saves the score in leader
    this also create file if file doesnt exit and writes
    pyhton dictionary'''
    name=input("what is your name?")
    leaders=load_scores() 
    leaders[name]=score

    with open("leaderboard.txt","w") as file:
        json.dump(leaders, file)

    return


def display_leaderboard(leaders):
    '''this prints the score and name if the player
    args: leaders in key value pair'''
    for name, score in leaders.items():
        print(name, ":", score)
    

