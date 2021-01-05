#Import methods
from IPython.display import clear_output
from itertools import permutations
import random

#Display the game board
def display_game(board):
    print('Here is your game board')
    print(board[0])
    print(board[1])
    print(board[2])
    
#Choose the position to put the marker
def position_choice():
    row = 'wrong'
    cell = 'wrong'
    while row not in ['1','2','3']:
        row = input('Choose the row you want to put your mark. Input 1, 2, or 3: ')
        if row not in ['1','2','3']:
            clear_output()
            print('Your input is not valid. Please make sure you enter 1, 2, or 3.')
        else:
            while cell not in ['1','2','3']:
                cell = input('Choose the column that you want to put your mark. Input 1, 2, or 3: ')
                if cell not in ['1','2','3']:
                    clear_output()
                    print('Your input is not valid. Please make sure you enter 1, 2, or 3.')
    return [int(row),int(cell)]
    
#Place the marker on the board
def player_placement(p1, row1, row2, row3, location):
    if p1 == True:
        if location[0] == 1:
            row1[location[1]-1] = 'X'
        if location[0] == 2:
            row2[location[1]-1] = 'X'
        if location[0] == 3:
            row3[location[1]-1] = 'X'
    if p1 == False:
        if location[0] == 1:
            row1[location[1]-1] = 'O'
        if location[0] == 2:
            row2[location[1]-1] = 'O'
        if location[0] == 3:
            row3[location[1]-1] = 'O'
    return row1, row2, row3
    
#Input player's name
def choose_player():
    print('The player who goes first is randomly chosen and always play X. The other player will play O.')
    p1_name = input("What is player 1's name: ")
    p2_name = input("What is player 2's name: ")
    return p1_name, p2_name
    
#Combine for a series of game playing steps
def game_play(p_val, name, all_pos, board):
    display_game(board)
    print(f"{name}, it's your turn.")
    pos = []
    while pos in all_pos:
        pos = position_choice()
        if pos in all_pos:
            clear_output()
            display_game(board)
            print("Sorry, this place is taken. Please put your mark elsewhere.")
            continue
        else:
            break
    gamelist = player_placement(p_val, board[0], board[1], board[2], pos)
    clear_output()
    return pos
    
#Check who wins
def check_win(p_pos, name, board):
    win = False
    win_list = [[[1,1],[1,2],[1,3]], [[2,1],[2,2],[2,3]], [[3,1],[3,2],[3,3]], [[1,1],[2,1],[3,1]], [[1,2],[2,2],[3,2]], [[1,3],[2,3],[3,3]], [[1,1],[2,2],[3,3]], [[1,3],[2,2],[3,1]]]  
    for i in range(0,len(win_list)):
        ref1 = list(permutations(win_list[i]))
        for k in range(0,len(ref1)):
            ref2 = list(ref1[k])
            win = all(item in p_pos for item in ref2)
            if win:
                display_game(board)
                print(f"Congratulations, {name}! You won!")
                break
        if win == True:
            break
    return win
    
#When the game is finished, choose to replay or not
def game_choice():
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input("Do you want to play again? Answer Y or N: ")
        if choice not in ['Y','N']:
            print("Sorry, I don't understand. Please answer Y or N.")
    if choice == 'Y':
        return True
    if choice == 'N':
        return False
        
#Combine all for the main game
def game_on():
    game_on = True
    while game_on:
        list1 = ['_','_','_']
        list2 = ['_','_','_']
        list3 = ['_','_','_']
        gamelist = (list1, list2, list3)
        position_list1 = []
        position_list2 = []
        all_position = [[]]
    
        clear_output()
        
        display_game(gamelist)
    
        player_name = choose_player()
        
        random_list = [0,1]
        p_random = random.choice(random_list)
        random_list.remove(p_random)
        
        clear_output()
        
        for i in range(1,10):
            if i%2 != 0:
                player1 = True
                playername = player_name[p_random]
                newpos = game_play(player1, playername, all_position, gamelist)
                all_position.append(newpos)
                position_list1.append(newpos)
                game_on = check_win(position_list1, playername, gamelist)
                if game_on:
                    break
            if i%2 == 0:
                player1 = False
                playername = player_name[int(random_list[0])]
                newpos = game_play(player1, playername, all_position, gamelist)
                all_position.append(newpos)
                position_list2.append(newpos)
                game_on = check_win(position_list2, playername, gamelist)
                if game_on:
                    break
        if game_on == False:
            display_game(gamelist)
            print("It's a tie!")
        game_on = game_choice()