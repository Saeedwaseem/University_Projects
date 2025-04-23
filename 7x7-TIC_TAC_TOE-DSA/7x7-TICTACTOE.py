# Function to print Tic Tac Toe
def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |     |     |     |     |     ")
    print("\t  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}".format(values[0], values[1], values[2], values[3], values[4], values[5], values[6]))
    print('\t ____|_____|_____|_____|_____|_____|_____')
    
    print("\t     |     |     |     |     |     |     ")
    print("\t  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}".format(values[7], values[8], values[9], values[10], values[11], values[12], values[13]))
    print('\t ____|_____|_____|_____|_____|_____|_____')
    
    print("\t     |     |     |     |     |     |     ")
    print("\t  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}".format(values[14], values[15], values[16], values[17], values[18], values[19], values[20]))
    print('\t ____|_____|_____|_____|_____|_____|_____')
    
    print("\t     |     |     |     |     |     |     ")
    print("\t  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}".format(values[21], values[22], values[23], values[24], values[25], values[26], values[27]))
    print('\t ____|_____|_____|_____|_____|_____|_____')
    
    print("\t     |     |     |     |     |     |     ")
    print("\t  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}".format(values[28], values[29], values[30], values[31], values[32], values[33], values[34]))
    print('\t ____|_____|_____|_____|_____|_____|_____')
    
    print("\t     |     |     |     |     |     |     ")
    print("\t  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}".format(values[35], values[36], values[37], values[38], values[39], values[40], values[41]))
    print('\t ____|_____|_____|_____|_____|_____|_____')
    
    print("\t     |     |     |     |     |     |     ")
    print("\t  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}".format(values[42], values[43], values[44], values[45], values[46], values[47], values[48]))
    print("\t     |     |     |     |     |     |     ")
    print("\n")

 
# Function to print the score-board
def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t                SCOREBOARD           ")
    print("\t--------------------------------")

    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])

    print("\t--------------------------------\n")

# Function to check if any player has won
def check_win(player_pos, cur_player):

    # All possible winning combinations
    soln = [#Rows
            [1, 2, 3, 4],     [2, 3, 4, 5],     [3, 4, 5, 6],     [4, 5, 6, 7],
            [8, 9, 10, 11],    [9, 10, 11, 12],    [10, 11, 12, 13], [11, 12, 13, 14],
            [15, 16, 17, 18], [16, 17, 18, 19], [17, 18, 19, 20], [18, 19, 20, 21],
            [22, 23, 24, 25], [23, 24, 25, 26], [24, 25, 26, 27], [25, 26, 27, 28],
            [29, 30, 31, 32], [30, 31, 32, 33], [31, 32, 33, 34], [32, 33, 34, 35],
            [36, 37, 38, 39], [37, 38, 39, 40], [38, 39, 40, 41], [39, 40, 41, 42],
            [43, 44, 45, 46], [44, 45, 46, 47], [45, 46, 47, 48], [46, 47, 48, 49],
            
            #Columns
            [1, 8, 15, 22],   [8, 15, 22, 29],  [15, 22, 29, 36], [22, 29, 36, 43],
            [2, 9, 16, 23],   [9, 16, 23, 30],  [16, 23, 30, 37], [23, 30, 37, 44],
            [3, 10, 17, 24],  [10, 17, 24, 31], [17, 24, 31, 38], [24, 31, 38, 45],
            [4, 11, 18, 25],  [11, 18, 25, 32], [18, 25, 32, 39], [25, 32, 39, 46],
            [5, 12, 19, 26],  [12, 19, 26, 33], [19, 26, 33, 40], [26, 33, 40, 47],
            [6, 13, 20, 27],  [13, 20, 27, 34], [20, 27, 34, 41], [27, 34, 41, 48],
            [7, 14, 21, 28],  [14, 21, 28, 35], [21, 28, 35, 42], [28, 35, 42, 49],
            
            #left to right diagnol
            [4, 12, 20, 28], 
            [3, 11, 19, 27],  [11, 19, 27, 35], 
            [2, 10, 18, 26],  [10, 18, 26, 34],  [18, 26, 34, 42],
            [1, 9, 17, 25],   [9, 17, 25, 33],  [17, 25, 33, 41], [25, 33, 41, 49],
            [8, 16 ,24, 32], [16, 24, 32, 40], [24, 32, 40, 48],
            [15, 23, 31, 39], [23, 31, 39, 47],
            [22, 30, 38, 46],
            
            #right to left diagnol
            [4, 10, 16, 22],
            [5, 11, 17, 23], [11, 17, 23, 29],
            [6, 12, 18, 24], [12, 18, 24, 30], [18, 24, 30, 36],
            [7, 13, 19, 25], [13, 19, 25, 31], [19, 25, 31, 37],[25, 31, 37, 43],
            [14, 20, 26, 32],[20, 26, 32, 38],[26, 32, 38, 44],
            [21, 27, 33, 39],[27, 33, 39, 45],
            [28, 34, 40, 46]
            ]

    # Loop to check if any winning combination is satisfied
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied     
    return False

# Function to check if the game is drawn
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 49:
        return True
    return False

# Function for a single game of Tic Tac Toe
def single_game(cur_player):

    # Represents the Tic Tac Toe
    values = [' ' for x in range(49)]
    
    # Stores the positions occupied by X and O
    player_pos = {'X':[], 'O':[]}
    
    # Game Loop for a single game of Tic Tac Toe
    while True:
        print_tic_tac_toe(values)
        
        # Try exception block for MOVE input
        try:
            print("Player ", cur_player, " turn. Which box? : ", end="")
            move = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue

        # Sanity check for MOVE inout
        if move < 1 or move > 49: # Changed to 1
            print("Wrong Input!!! Try Again")
            continue

        # Check if the box is not occupied already
        if values[move-1] != ' ':
            print("Place already filled. Try again!!")
            continue

        # Update game information

        # Updating grid status 
        values[move-1] = cur_player

        # Updating player positions
        player_pos[cur_player].append(move)

        # Function call for checking win
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Player ", cur_player, " has won the game!!")
            print("\n")
            return cur_player

        # Function call for checking draw game
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Game Drawn")
            print("\n")
            return 'D'

        # Switch player moves
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'

if __name__ == "__main__": # Added if __name__ == "__main__":

    print("Player 1")
    player1 = input("Enter the name : ")
    print("\n")

    print("Player 2")
    player2 = input("Enter the name : ")
    print("\n")
    
    # Stores the player who chooses X and O
    cur_player = player1

    # Stores the choice of players
    player_choice = {'X' : "", 'O' : ""}

    # Stores the options
    options = ['X', 'O']

    # Stores the scoreboard
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)

    # Game Loop for a series of Tic Tac Toe
    # The loop runs until the players quit 
    while True:

        # Player choice Menu
        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")

        # Try exception for CHOICE input
        try:
            choice = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue

        # Conditions for player choice 
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1

        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
        
        elif choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break

        else:
            print("Wrong Choice!!!! Try Again\n")

        # Stores the winner in a single game of Tic Tac Toe
        winner = single_game(options[choice-1])
        
        # Edits the scoreboard according to the winner
        if winner != 'D' :
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1

        print_scoreboard(score_board)
        # Switch player who chooses X or O
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1
