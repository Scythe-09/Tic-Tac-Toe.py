#Tic Tac Toe
import random
print('Welcome to Tic Tac Toe!')
print('''Format:
 A3 | B3 | C3
-------------
 A2 | B2 | C2
-------------
 A1 | B1 | C1
''')
board = [' ', ' ', ' ',
        ' ', ' ', ' ',
        ' ', ' ', ' ']
Player1_wins = 0
Player2_wins = 0
Player_wins = 0
Computer_wins = 0
Ties = 0
notations = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
play_again = None
user = None
def whole_board():
    print(f'\t {board[0]} | {board[1]} | {board[2]} ')
    print(f'\t---|---|---')
    print(f'\t {board[3]} | {board[4]} | {board[5]} ')
    print(f'\t---|---|---')
    print(f'\t {board[6]} | {board[7]} | {board[8]} ')
def player1(user):
    while True:
        if ' ' not in board:
            return
        elif user == 'computer' or user == 'computer ':
            player_one = input('Player pick a position: ').upper()
        elif user == 'player' or user == 'player ':
            player_one = input('Player1 pick a position: ').upper()
        if player_one in notations:
            if player_one == 'A1' and board[6] == ' ':
                board[6] = 'X'
                if ' ' not in board:
                    return False
                else:
                    return
            elif player_one == 'A2' and board[3] == ' ':
                board[3] = 'X'
                if ' ' not in board:
                    return False
                else:
                    return
            elif player_one == 'A3' and board[0] == ' ':
                board[0] = 'X'
                if ' ' not in board:
                    return False
                else:
                    return
            elif player_one == 'B1' and board[7] == ' ':
                board[7] = 'X'
                if ' ' not in board:
                    return False
                else:
                    return
            elif player_one == 'B2' and board[4] == ' ':
                board[4] = 'X'
                if ' ' not in board:
                    return False
                else:
                    return
            elif player_one == 'B3' and board[1] == ' ':
                board[1] = 'X'
                if ' ' not in board:
                    return False
                else:
                    return
            elif player_one == 'C1' and board[8] == ' ':
                board[8] = 'X'
                if ' ' not in board:
                    return False
                else:
                    return
            elif player_one == 'C2' and board[5] == ' ':
                board[5] = 'X'
                if ' ' not in board:
                    return False
                else:
                    return
            elif player_one == 'C3' and board[2] == ' ':
                board[2] = 'X'
                if ' ' not in board:
                    return False
                else:
                    return
            else:
                print('This spot has been taken!')
                continue
        else:
            print('Please type a valid answer!')
            continue
def player2():
    while True:
        if ' ' not in board:
            return False
        else:
            None
        player_two = input('Player2 pick a position: ').upper()
        if player_two in notations:
            if player_two == 'A1' and board[6] == ' ':
                board[6] = 'O'
                return
            elif player_two == 'A2' and board[3] == ' ':
                board[3] = 'O'
                return
            elif player_two == 'A3' and board[0] == ' ':
                board[0] = 'O'
                return
            elif player_two == 'B1' and board[7] == ' ':
                board[7] = 'O'
                return
            elif player_two == 'B2' and board[4] == ' ':
                board[4] = 'O'
                return
            elif player_two == 'B3' and board[1] == ' ':
                board[1] = 'O'
                return
            elif player_two == 'C1' and board[8] == ' ':
                board[8] = 'O'
                return
            elif player_two == 'C2' and board[5] == ' ':
                board[5] = 'O'
                return
            elif player_two == 'C3' and board[2] == ' ':
                board[2] = 'O'
                return
            else:
                print('This spot has been taken!')
                continue
        else:
            print('Please type a valid answer!')
            continue
def computer(difficulty):
    while True:
        computer_pick = random.randrange(9)
        if difficulty == 'easy' or difficulty == 'easy ':
            if computer_pick == 4 and board[4] == ' ':
                board[4] = 'O'
                return False
            elif computer_pick == 0 and board[0] == ' ':
                board[0] = 'O'
                return False
            elif computer_pick == 1 and board[1] == ' ':
                board[1] = 'O'
                return False
            elif computer_pick == 2 and board[2] == ' ':
                board[2] = 'O'
                return False
            elif computer_pick == 3 and board[3] == ' ':
                board[3] = 'O'
                return False
            elif computer_pick == 5 and board[5] == ' ':
                board[5] = 'O'
                return False
            elif computer_pick == 6 and board[6] == ' ':
                board[6] = 'O'
                return False
            elif computer_pick == 7 and board[7] == ' ':
                board[7] = 'O'
                return False
            elif computer_pick == 8 and board[8] == ' ':
                board[8] = 'O'
                return False
            elif ' ' not in board:
                return True
            else:
                continue
        elif difficulty == 'medium' or difficulty == 'medium ':
            if board[0] == board[1] and board[0] == 'O' and board[2] == ' ':
                board[2] = 'O'
                return False
            elif board[1] == board[2] and board[1] == 'O' and board[0] == ' ':
                board[0] = 'O'
                return False
            elif board[0] == board[2] and board[0] == 'O' and board[1] == ' ':
                board[1] = 'O'
                return False
            elif board[4] == board[3] and board[4] == 'O' and board[5] == ' ':
                board[5] = 'O'
                return False
            elif board[4] == board[5] and board[5] == 'O' and board[3] == ' ':
                board[3] = 'O'
                return False
            elif board[5] == board[3] and board[5] == 'O' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif board[6] == board[7] and board[6] == 'O' and board[8] == ' ':
                board[8] = 'O'
                return False
            elif board[7] == board[8] and board[7] == 'O' and board[6] == ' ':
                board[6] = 'O'
                return False
            elif board[6] == board[8] and board[8] == 'O' and board[7] == ' ':
                board[7] = 'O'
                return False
            elif board[0] == board[3] and board[3] == 'O' and board[6] == ' ':
                board[6] = 'O'
                return False
            elif board[6] == board[3] and board[6] == 'O' and board[0] == ' ':
                board[0] = 'O'
                return False
            elif board[0] == board[6] and board[6] == 'O' and board[3] == ' ':
                board[3] = 'O'
                return False
            elif board[1] == board[4] and board[4] == 'O' and board[7] == ' ':
                board[7] = 'O'
                return False
            elif board[4] == board[7] and board[4] == 'O' and board[1] == ' ':
                board[1] = 'O'
                return False
            elif board[1] == board[7] and board[7] == 'O' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif board[2] == board[5] and board[5] == 'O' and board[8] == ' ':
                board[8] = 'O'
                return False
            elif board[8] == board[5] and board[5] == 'O' and board[2] == ' ':
                board[2] = 'O'
                return False
            elif board[2] == board[8] and board[8] == 'O' and board[5] == ' ':
                board[5] = 'O'
                return False
            elif board[4] == board[0] and board[4] == 'O' and board[8] == ' ':
                board[8] = 'O'
                return False
            elif board[8] == board[4] and board[4] == 'O' and board[0] == ' ':
                board[0] = 'O'
                return False
            elif board[8] == board[0] and board[8] == 'O' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif board[2] == board[4] and board[4] == 'O' and board[6] == ' ':
                board[6] = 'O'
                return False
            elif board[6] == board[4] and board[4] == 'O' and board[2] == ' ':
                board[2] = 'O'
                return False
            elif board[6] == board[2] and board[2] == 'O' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif computer_pick == 4 and board[4] == ' ':
                board[4] = 'O'
                return False
            elif computer_pick == 0 and board[0] == ' ':
                board[0] = 'O'
                return False
            elif computer_pick == 1 and board[1] == ' ':
                board[1] = 'O'
                return False
            elif computer_pick == 2 and board[2] == ' ':
                board[2] = 'O'
                return False
            elif computer_pick == 3 and board[3] == ' ':
                board[3] = 'O'
                return False
            elif computer_pick == 5 and board[5] == ' ':
                board[5] = 'O'
                return False
            elif computer_pick == 6 and board[6] == ' ':
                board[6] = 'O'
                return False
            elif computer_pick == 7 and board[7] == ' ':
                board[7] = 'O'
                return False
            elif computer_pick == 8 and board[8] == ' ':
                board[8] = 'O'
                return False
            elif ' ' not in board:
                return True
            else:
                continue
        elif difficulty == 'hard' or difficulty == 'hard ':
            if board[0] == board[1] and board[0] == 'O' and board[2] == ' ':
                board[2] = 'O'
                return False
            elif board[1] == board[2] and board[1] == 'O' and board[0] == ' ':
                board[0] = 'O'
                return False
            elif board[0] == board[2] and board[0] == 'O' and board[1] == ' ':
                board[1] = 'O'
                return False
            elif board[4] == board[3] and board[4] == 'O' and board[5] == ' ':
                board[5] = 'O'
                return False
            elif board[4] == board[5] and board[5] == 'O' and board[3] == ' ':
                board[3] = 'O'
                return False
            elif board[5] == board[3] and board[5] == 'O' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif board[6] == board[7] and board[6] == 'O' and board[8] == ' ':
                board[8] = 'O'
                return False
            elif board[7] == board[8] and board[7] == 'O' and board[6] == ' ':
                board[6] = 'O'
                return False
            elif board[6] == board[8] and board[8] == 'O' and board[7] == ' ':
                board[7] = 'O'
                return False
            elif board[0] == board[3] and board[3] == 'O' and board[6] == ' ':
                board[6] = 'O'
                return False
            elif board[6] == board[3] and board[6] == 'O' and board[0] == ' ':
                board[0] = 'O'
                return False
            elif board[0] == board[6] and board[6] == 'O' and board[3] == ' ':
                board[3] = 'O'
                return False
            elif board[1] == board[4] and board[4] == 'O' and board[7] == ' ':
                board[7] = 'O'
                return False
            elif board[4] == board[7] and board[4] == 'O' and board[1] == ' ':
                board[1] = 'O'
                return False
            elif board[1] == board[7] and board[7] == 'O' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif board[2] == board[5] and board[5] == 'O' and board[8] == ' ':
                board[8] = 'O'
                return False
            elif board[8] == board[5] and board[5] == 'O' and board[2] == ' ':
                board[2] = 'O'
                return False
            elif board[2] == board[8] and board[8] == 'O' and board[5] == ' ':
                board[5] = 'O'
                return False
            elif board[4] == board[0] and board[4] == 'O' and board[8] == ' ':
                board[8] = 'O'
                return False
            elif board[8] == board[4] and board[4] == 'O' and board[0] == ' ':
                board[0] = 'O'
                return False
            elif board[8] == board[0] and board[8] == 'O' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif board[2] == board[4] and board[4] == 'O' and board[6] == ' ':
                board[6] = 'O'
                return False
            elif board[6] == board[4] and board[4] == 'O' and board[2] == ' ':
                board[2] = 'O'
                return False
            elif board[6] == board[2] and board[2] == 'O' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif board[0] == board[1] and board[0] == 'X' and board[2] == ' ':
                board[2] = 'O'
                return False
            elif board[1] == board[2] and board[1] == 'X' and board[0] == ' ':
                board[0] = 'O'
                return False
            elif board[0] == board[2] and board[0] == 'X' and board[1] == ' ':
                board[1] = 'O'
                return False
            elif board[4] == board[3] and board[4] == 'X' and board[5] == ' ':
                board[5] = 'O'
                return False
            elif board[4] == board[5] and board[5] == 'X' and board[3] == ' ':
                board[3] = 'O'
                return False
            elif board[5] == board[3] and board[5] == 'X' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif board[6] == board[7] and board[6] == 'X' and board[8] == ' ':
                board[8] = 'O'
                return False
            elif board[7] == board[8] and board[7] == 'X' and board[6] == ' ':
                board[6] = 'O'
                return False
            elif board[6] == board[8] and board[8] == 'X' and board[7] == ' ':
                board[7] = 'O'
                return False
            elif board[0] == board[3] and board[3] == 'X' and board[6] == ' ':
                board[6] = 'O'
                return False
            elif board[6] == board[3] and board[6] == 'X' and board[0] == ' ':
                board[0] = 'O'
                return False
            elif board[0] == board[6] and board[6] == 'X' and board[3] == ' ':
                board[3] = 'O'
                return False
            elif board[1] == board[4] and board[4] == 'X' and board[7] == ' ':
                board[7] = 'O'
                return False
            elif board[4] == board[7] and board[4] == 'X' and board[1] == ' ':
                board[1] = 'O'
                return False
            elif board[1] == board[7] and board[7] == 'X' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif board[2] == board[5] and board[5] == 'X' and board[8] == ' ':
                board[8] = 'O'
                return False
            elif board[8] == board[5] and board[5] == 'X' and board[2] == ' ':
                board[2] = 'O'
                return False
            elif board[2] == board[8] and board[8] == 'X' and board[5] == ' ':
                board[5] = 'O'
                return False
            elif board[4] == board[0] and board[4] == 'X' and board[8] == ' ':
                board[8] = 'O'
                return False
            elif board[8] == board[4] and board[4] == 'X' and board[0] == ' ':
                board[0] = 'O'
                return False
            elif board[8] == board[0] and board[8] == 'X' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif board[2] == board[4] and board[4] == 'X' and board[6] == ' ':
                board[6] = 'O'
                return False
            elif board[6] == board[4] and board[4] == 'X' and board[2] == ' ':
                board[2] = 'O'
                return False
            elif board[6] == board[2] and board[2] == 'X' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif computer_pick == 4 and board[4] == ' ':
                board[4] = 'O'
                return False
            elif computer_pick == 0 and board[0] == ' ':
                board[0] = 'O'
                return False
            elif computer_pick == 1 and board[1] == ' ':
                board[1] = 'O'
                return False
            elif computer_pick == 2 and board[2] == ' ':
                board[2] = 'O'
                return False
            elif computer_pick == 3 and board[3] == ' ':
                board[3] = 'O'
                return False
            elif computer_pick == 5 and board[5] == ' ':
                board[5] = 'O'
                return False
            elif computer_pick == 6 and board[6] == ' ':
                board[6] = 'O'
                return False
            elif computer_pick == 7 and board[7] == ' ':
                board[7] = 'O'
                return False
            elif computer_pick == 8 and board[8] == ' ':
                board[8] = 'O'
                return False
            elif ' ' not in board:
                return True
            else:
                continue
        elif difficulty == 'impossible' or difficulty == 'impossible ':
            if (board.count(' ') == 8 or board.count(' ') == 9) and board[0] == 'X' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[8] == 'X' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[4] == 'X' and board[8] == ' ':
                board[8] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[4] == 'X' and board[0] == ' ':
                board[0] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[3] == 'X' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[6] == 'X' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[4] == 'X' and board[6] == ' ':
                board[6] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[4] == 'X' and board[3] == ' ':
                board[3] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[0] == 'X' and board[1] == ' ':
                board[1] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[2] == 'X' and board[1] == ' ':
                board[1] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[1] == 'X' and board[2] == ' ':
                board[2] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[1] == 'X' and board[0] == ' ':
                board[0] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[3] == 'X' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[5] == 'X' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[4] == 'X' and board[5] == ' ':
                board[5] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[4] == 'X' and board[3] == ' ':
                board[3] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[6] == 'X' and board[7] == ' ':
                board[7] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[8] == 'X' and board[7] == ' ':
                board[7] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[8] == 'X' and board[7] == ' ':
                board[7] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[8] == 'X' and board[6] == ' ':
                board[6] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[6] == 'X' and board[3] == ' ':
                board[3] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[0] == 'X' and board[3] == ' ':
                board[3] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[3] == 'X' and board[6] == ' ':
                board[6] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[3] == 'X' and board[0] == ' ':
                board[0] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[1] == 'X' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[7] == 'X' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[4] == 'X' and board[7] == ' ':
                board[7] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[4] == 'X' and board[1] == ' ':
                board[1] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[2] == 'X' and board[5] == ' ':
                board[5] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[8] == 'X' and board[5] == ' ':
                board[5] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[5] == 'X' and board[8] == ' ':
                board[8] = 'O'
                return False
            elif (board.count(' ') == 8 or board.count(' ') == 9) and board[5] == 'X' and board[2] == ' ':
                board[2] = 'O'
                return False
            elif board[0] == board[1] and board[0] == 'O' and board[2] == ' ':
                board[2] = 'O'
                return False
            elif board[1] == board[2] and board[1] == 'O' and board[0] == ' ':
                board[0] = 'O'
                return False
            elif board[0] == board[2] and board[0] == 'O' and board[1] == ' ':
                board[1] = 'O'
                return False
            elif board[4] == board[3] and board[4] == 'O' and board[5] == ' ':
                board[5] = 'O'
                return False
            elif board[4] == board[5] and board[5] == 'O' and board[3] == ' ':
                board[3] = 'O'
                return False
            elif board[5] == board[3] and board[5] == 'O' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif board[6] == board[7] and board[6] == 'O' and board[8] == ' ':
                board[8] = 'O'
                return False
            elif board[7] == board[8] and board[7] == 'O' and board[6] == ' ':
                board[6] = 'O'
                return False
            elif board[6] == board[8] and board[8] == 'O' and board[7] == ' ':
                board[7] = 'O'
                return False
            elif board[0] == board[3] and board[3] == 'O' and board[6] == ' ':
                board[6] = 'O'
                return False
            elif board[6] == board[3] and board[6] == 'O' and board[0] == ' ':
                board[0] = 'O'
                return False
            elif board[0] == board[6] and board[6] == 'O' and board[3] == ' ':
                board[3] = 'O'
                return False
            elif board[1] == board[4] and board[4] == 'O' and board[7] == ' ':
                board[7] = 'O'
                return False
            elif board[4] == board[7] and board[4] == 'O' and board[1] == ' ':
                board[1] = 'O'
                return False
            elif board[1] == board[7] and board[7] == 'O' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif board[2] == board[5] and board[5] == 'O' and board[8] == ' ':
                board[8] = 'O'
                return False
            elif board[8] == board[5] and board[5] == 'O' and board[2] == ' ':
                board[2] = 'O'
                return False
            elif board[2] == board[8] and board[8] == 'O' and board[5] == ' ':
                board[5] = 'O'
                return False
            elif board[4] == board[0] and board[4] == 'O' and board[8] == ' ':
                board[8] = 'O'
                return False
            elif board[8] == board[4] and board[4] == 'O' and board[0] == ' ':
                board[0] = 'O'
                return False
            elif board[8] == board[0] and board[8] == 'O' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif board[2] == board[4] and board[4] == 'O' and board[6] == ' ':
                board[6] = 'O'
                return False
            elif board[6] == board[4] and board[4] == 'O' and board[2] == ' ':
                board[2] = 'O'
                return False
            elif board[6] == board[2] and board[2] == 'O' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif board[0] == board[1] and board[0] == 'X' and board[2] == ' ':
                board[2] = 'O'
                return False
            elif board[1] == board[2] and board[1] == 'X' and board[0] == ' ':
                board[0] = 'O'
                return False
            elif board[0] == board[2] and board[0] == 'X' and board[1] == ' ':
                board[1] = 'O'
                return False
            elif board[4] == board[3] and board[4] == 'X' and board[5] == ' ':
                board[5] = 'O'
                return False
            elif board[4] == board[5] and board[5] == 'X' and board[3] == ' ':
                board[3] = 'O'
                return False
            elif board[5] == board[3] and board[5] == 'X' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif board[6] == board[7] and board[6] == 'X' and board[8] == ' ':
                board[8] = 'O'
                return False
            elif board[7] == board[8] and board[7] == 'X' and board[6] == ' ':
                board[6] = 'O'
                return False
            elif board[6] == board[8] and board[8] == 'X' and board[7] == ' ':
                board[7] = 'O'
                return False
            elif board[0] == board[3] and board[3] == 'X' and board[6] == ' ':
                board[6] = 'O'
                return False
            elif board[6] == board[3] and board[6] == 'X' and board[0] == ' ':
                board[0] = 'O'
                return False
            elif board[0] == board[6] and board[6] == 'X' and board[3] == ' ':
                board[3] = 'O'
                return False
            elif board[1] == board[4] and board[4] == 'X' and board[7] == ' ':
                board[7] = 'O'
                return False
            elif board[4] == board[7] and board[4] == 'X' and board[1] == ' ':
                board[1] = 'O'
                return False
            elif board[1] == board[7] and board[7] == 'X' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif board[2] == board[5] and board[5] == 'X' and board[8] == ' ':
                board[8] = 'O'
                return False
            elif board[8] == board[5] and board[5] == 'X' and board[2] == ' ':
                board[2] = 'O'
                return False
            elif board[2] == board[8] and board[8] == 'X' and board[5] == ' ':
                board[5] = 'O'
                return False
            elif board[4] == board[0] and board[4] == 'X' and board[8] == ' ':
                board[8] = 'O'
                return False
            elif board[8] == board[4] and board[4] == 'X' and board[0] == ' ':
                board[0] = 'O'
                return False
            elif board[8] == board[0] and board[8] == 'X' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif board[2] == board[4] and board[4] == 'X' and board[6] == ' ':
                board[6] = 'O'
                return False
            elif board[6] == board[4] and board[4] == 'X' and board[2] == ' ':
                board[2] = 'O'
                return False
            elif board[6] == board[2] and board[2] == 'X' and board[4] == ' ':
                board[4] = 'O'
                return False
            elif computer_pick == 4 and board[4] == ' ':
                board[4] = 'O'
                return False
            elif computer_pick == 0 and board[0] == ' ':
                board[0] = 'O'
                return False
            elif computer_pick == 1 and board[1] == ' ':
                board[1] = 'O'
                return False
            elif computer_pick == 2 and board[2] == ' ':
                board[2] = 'O'
                return False
            elif computer_pick == 3 and board[3] == ' ':
                board[3] = 'O'
                return False
            elif computer_pick == 5 and board[5] == ' ':
                board[5] = 'O'
                return False
            elif computer_pick == 6 and board[6] == ' ':
                board[6] = 'O'
                return False
            elif computer_pick == 7 and board[7] == ' ':
                board[7] = 'O'
                return False
            elif computer_pick == 8 and board[8] == ' ':
                board[8] = 'O'
                return False
            elif ' ' not in board:
                return False
            else:
                continue
        else:
            while difficulty != 'easy' or difficulty != 'easy ' or difficulty != 'medium' or difficulty != 'medium ' or difficulty != 'hard' or difficulty != 'hard ' or difficulty != 'impossible' or difficulty != 'impossible ':
                difficulty = random.randrange('easy', 'hard', 'medium', 'impossible', 'easy ', 'medium ', 'hard ', 'impossible ')
            continue
def checking_if_player1_or_player_won(user):
    global play_again
    global Player1_wins
    global Player_wins
    if (board[2] == board[4] == board[6] and board[2] == 'X') or (board[0] == board[4] == board[8] and board[0] == 'X') or (board[6] == board[7] == board[8] and board[6] == 'X') or (board[3] == board[4] == board[5] and board[3] == 'X') or (board[0] == board[1] == board[2] and board[0] == 'X') or (board[2] == board[5] == board[8] and board[2] == 'X') or (board[1] == board[4] == board[7] and board[1] == 'X') or (board[0] == board[3] == board[6] and board[0] == 'X'):
        if user == 'player' or user == 'player ':
            print(f'Player1 Wins!')
            Player1_wins += 1
        elif user == 'computer' or user == 'computer ':
            print(f'Player Wins!')
            Player_wins += 1
        while True:
            play_again = input('Do you want to play again [Yes/No]? ').lower()
            if play_again == 'yes' or play_again == 'yes ':
                return True
            elif play_again == 'no' or play_again == 'no ':
                return True
            else:
                print('Please type a valid answer!')
                continue
    else:
        return False
def checking_if_player2_or_computer_won(user):
    global play_again
    global Player2_wins
    global Computer_wins
    if (board[2] == board[4] == board[6] and board[2] == 'O') or (board[0] == board[4] == board[8] and board[0] == 'O') or (board[6] == board[7] == board[8] and board[6] == 'O') or (board[3] == board[4] == board[5] and board[3] == 'O') or (board[0] == board[1] == board[2] and board[0] == 'O') or (board[2] == board[5] == board[8] and board[2] == 'O') or (board[1] == board[4] == board[7] and board[1] == 'O') or (board[0] == board[3] == board[6] and board[0] == 'O'):
        if user == 'computer' or user == 'computer ':
            print(f'Player2 Wins!')
            Player2_wins += 1
        elif user == 'player' or user == 'player ':
            print(f'Computer Wins!')
            Computer_wins += 1
        while True:
            play_again = input('Do you want to play again [Yes/No]? ').lower()
            if play_again == 'yes' or play_again == 'yes ':
                return True
            elif play_again == 'no' or play_again == 'no ':
                return True
            else:
                print('Please type a valid answer!')
                continue
    else:
        return False
def checking_if_tie(checking_if_player1_or_player_won, checking_if_player2_or_computer_won):
    global play_again
    global Ties
    if (' ' not in board) and (checking_if_player1_or_player_won == False and checking_if_player2_or_computer_won == False):
        print('It\'s a tie!')
        Ties += 1
        while True:
            play_again = input('Do you want to play again [Yes/No]? ').lower()
            if play_again == 'yes' or play_again == 'yes ':
                return True
            elif play_again == 'no' or play_again == 'no ':
                return True
            else:
                print('Please type a valid answer!')
                continue
    else:
        return
def guest():
    global user
    user = input('Choose a mode [Player / Computer]: ').lower()
def scores(user):
    if user == 'player' or user == 'player ':
        print('\t _______________________')
        print('\t|\tSCOREBOARD\t|')
        print(f'\t|Player1 = {Player1_wins}\t\t|')
        print(f'\t|Player2 = {Player2_wins}\t\t|')
        print(f'\t|Ties = {Ties}   \t\t|')
        print('\t|_______________________|')
        print('Goodbye!')
        quit()
    elif user == 'computer' or user == 'computer ':
        print('\t _______________________')
        print('\t|\tSCOREBOARD\t|')
        print(f'\t|Player = {Player_wins}\t\t|')
        print(f'\t|Computer = {Computer_wins}\t\t|')
        print(f'\t|Ties = {Ties}   \t\t|')
        print('\t|_______________________|')
        print('Goodbye!')
        quit()
guest()
while True:
    if user == 'player' or user == 'player ':
        Player1_wins = 0
        Player2_wins = 0
        Ties = 0
        while True:
            if play_again == 'yes' or play_again == 'yes ':
                board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                play_again = None
                while True:
                    guest()
                    if user == 'player' or user == 'player ' or user == 'computer' or user == 'computer ':
                        break
                    else:
                        print('Please type a valid answer!')
                        continue
                if user == 'player' or user == 'player ':
                    continue
                elif user == 'computer' or user == 'computer ':
                    break
            elif play_again == 'no' or play_again == 'no ':
                scores(user)
            else:
                player1(user)
                whole_board()
                if checking_if_player1_or_player_won(user) == True:
                    continue
                elif checking_if_tie(checking_if_player1_or_player_won(user), checking_if_player2_or_computer_won(user)) == True:
                    continue
                else:
                    player2()
                    whole_board()
                    checking_if_player2_or_computer_won(user)
        continue
    elif user == 'computer' or user == 'computer ':
        Player_wins = 0
        Computer_wins = 0
        Ties = 0
        while True:
            difficulty = input('Choose a difficulty [Easy/Medium/Hard/Impossible]: ').lower()
            if difficulty == 'easy' or difficulty == 'easy ' or difficulty == 'medium' or difficulty == 'medium ' or difficulty == 'hard' or difficulty == 'hard ' or difficulty == 'impossible' or difficulty == 'impossible ':
                while True:
                    player1(user)
                    if (board[2] == board[4] == board[6] and board[2] == 'X') or (board[0] == board[4] == board[8] and board[0] == 'X') or (board[6] == board[7] == board[8] and board[6] == 'X') or (board[3] == board[4] == board[5] and board[3] == 'X') or (board[0] == board[1] == board[2] and board[0] == 'X') or (board[2] == board[5] == board[8] and board[2] == 'X') or (board[1] == board[4] == board[7] and board[1] == 'X') or (board[0] == board[3] == board[6] and board[0] == 'X'):
                        None
                    else:
                        computer(difficulty)
                    whole_board()
                    checking_if_player1_or_player_won(user)
                    if checking_if_player1_or_player_won == True:
                        None
                    else:
                        checking_if_player2_or_computer_won(user)
                    if play_again == 'yes' or play_again == 'yes ' or play_again == 'no' or play_again == 'no ':
                        None
                    else:
                        checking_if_tie(checking_if_player1_or_player_won(user), checking_if_player2_or_computer_won(user))
                    if play_again == 'yes' or play_again == 'yes ':
                        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                        play_again = None
                        while True:
                            guest()
                            if user == 'player' or user == 'player ' or user == 'computer' or user == 'computer ':
                                break
                            else:
                                print('Please type a valid answer!')
                                continue
                        break
                    elif play_again == 'no' or play_again == 'no ':
                        scores(user)
                    else:
                        None
                if user == 'player' or user == 'player ':
                    break
                elif user == 'computer' or user == 'computer ':
                    continue
            else:
                print('Please type a valid answer!')
                continue
        continue
    else:
        print('Please type valid answer!')
        guest()
        continue
