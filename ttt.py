import random
board_spaces = [' ' for x in range(10)]
x = ["x"]

def space_is_free(pos):
    return board_spaces[pos] == ' '

def print_board():
    print(" " + board_spaces[1] + ' | ' + board_spaces[2] + ' | ' + board_spaces[3])
    print("---+---+---")
    print(" " + board_spaces[4] + ' | ' + board_spaces[5] + ' | ' + board_spaces[6])
    print("---+---+---")
    print(" " + board_spaces[7] + ' | ' + board_spaces[8] + ' | ' + board_spaces[9])

def is_winner(board_spaces, letter):
    return (board_spaces[3] == letter and board_spaces[2] == letter and board_spaces[1] == letter) or\
    (board_spaces[1] == letter and board_spaces[4] == letter and board_spaces[7] == letter) or\
    (board_spaces[2] == letter and board_spaces[5] == letter and board_spaces[8] == letter) or\
    (board_spaces[3] == letter and board_spaces[6] == letter and board_spaces[9] == letter) or\
    (board_spaces[3] == letter and board_spaces[5] == letter and board_spaces[7] == letter) or\
    (board_spaces[1] == letter and board_spaces[5] == letter and board_spaces[9] == letter)

def player_move():
    while True:
        pos = input("Select a position (1-9): ")
        pos = int(pos)
        if space_is_free(pos) is True:
            board_spaces[pos] = "X"
            break
        else:
            print("That space is taken!")
            continue

def free_spaces(board_spaces):
    x = free_pool = []

    for i in range(1, 10):
        if board_spaces[i] == " ":
            free_pool.append(i)
        else:
            continue
    return x

def comp_move():
    selection = random.choices(free_spaces(board_spaces))
    loc = int(selection[0])
    board_spaces[loc] = "O"

def select_random(board):
    pass

def is_board_full(board):
    if " " not in board[1:10]:
        print_board()
        return True
    else:
        return False


print("\nWelcome to Tic Tac Toe!")
print("You are 'X' and computer is 'O'\n")
x = free_spaces(board_spaces)

while not is_board_full(board_spaces):
    print_board()

    player_move()

    if is_winner(board_spaces, "X") or is_winner(board_spaces, "O") is True:
        print_board()
        if board_spaces.count("X") > board_spaces.count("O"):
            print("\nYou win!!!")
            exit()
        else:
            print("\nComputer wins!")
            exit()

    try:
        comp_move()
        print("\n")
    except IndexError:
        pass

    if is_winner(board_spaces, "X") or is_winner(board_spaces, "O") is True:
        print("\n")
        print_board()
        if board_spaces.count("X") > board_spaces.count("O"):
            print("\nYou win!!!")
            exit()
        else:
            print("\nComputer wins!")
            exit() 







print("\nTie game!")
