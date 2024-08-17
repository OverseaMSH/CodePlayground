# from termcolor import colored
from os import system,name
from termcolor import colored
player, computer = None, None
board = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
compMoveAlg = ((2, 4, 6, 8), (5,), (1, 3, 7, 9))
wins = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
playerChoice, computerChoice = [], []
while True:
    selection = input(colored("Choose X or O : ","yellow"))
    if "x" in selection or "X" in selection:
        player = "X"
        computer = "O"
        break
    elif "o" in selection or "O" in selection:
        player = "O"
        computer = "X"
        break
    else:
        print(colored("Invalid, please try again and choose X or O","yellow"))


def printBoard(player, computer, playerChoice, computerChoice):
    for row in board.keys():
        if row % 3 != 0:
            if board[row] == player:
                print(colored("[X]", "green"), end='')
            elif board[row] == computer:
                print(colored("[O]", "red"), end='')
            else:
                print(colored(f"[{board[row]}]", "white"), end='')
        else:
            if board[row] == player:
                print(colored("[X]", "green"))
            elif board[row] == computer:
                print(colored("[O]", "red"))
            else:
                print(colored(f"[{board[row]}]", "white"), end='\n')



def checkWinner(player, computer, board):
    for tup in wins:
        playerCounter, computerCounter = 0, 0
        for index in tup:
            if board[index] == player:
                playerCounter += 1
            if board[index] == computer:
                computerCounter += 1
            if playerCounter == 3:
                print(colored("You won","green"))
                return True
            elif computerCounter == 3:
                print(colored("You lost","red"))
                return True
    return False

def checkDraw(board):
    for key in board:
        if isinstance(board[key], int):
            return False  # If any position is empty, game is not a draw
    print(colored("It's a draw","yellow"))
    return True
def tryWin(player, computer):
    index, moved = -1, False
    for tup in wins:
        if board[tup[0]] == computer and board[tup[1]] == computer and board[tup[2]] != player:
            index, moved = tup[2], True
            break
        elif board[tup[0]] == computer and board[tup[2]] == computer and board[tup[1]] != player:
            index, moved = tup[1], True
            break

        elif board[tup[1]] == computer and board[tup[2]] == computer and board[tup[0]] != player:
            index, moved = tup[0], True
            break
        else:
            pass
    return index, moved


def prevLose(player, computer):
    index, moved = -1, False
    for tup in wins:
        if board[tup[0]] == player and board[tup[1]] == player and board[tup[2]] != computer:
            index, moved = tup[2], True
            break
        elif board[tup[0]] == player and board[tup[2]] == player and board[tup[1]] != computer:
            index, moved = tup[1], True
            break

        elif board[tup[1]] == player and board[tup[2]] == player and board[tup[0]] != computer:
            index, moved = tup[0], True
            break
        else:
            pass
    return index, moved


def tryMove(player, computer):
    moved = False
    i = None
    for tup in compMoveAlg:
        for index in tup:
            if board[index] != player and board[index] != computer:
                i = index
                moved = True
                break
    return i, moved
def printEmptyBoard():
    for row in board.keys():
        if row % 3 != 0:
            print(colored(f"[{board[row]}]","white"), end='')
        else:
            print(colored(f"[{board[row]}]","white"), end='\n')

printEmptyBoard()
while True:

    playerChoice = input(colored("choose a number between 1 and 9 : ","yellow"))
    if name == "nt":
        system("cls")
    else:
        system("clear")
    if int(playerChoice) in board.keys() and isinstance(board[int(playerChoice)], int):
        board[int(playerChoice)] = player
        if checkWinner(player, computer, board):
            printBoard(player, computer, playerChoice, computerChoice)
            break  # Game ends if there's a winner
        elif checkDraw(board):
            printBoard(player, computer, playerChoice, computerChoice)
            break  # Game ends if it's a draw
        else:
            if tryWin(player, computer)[1] == True:
                board[tryWin(player, computer)[0]] = computer
                if checkWinner(player, computer, board):
                    printBoard(player, computer, playerChoice, computerChoice)
                    break  # Game ends if there's a winner
            elif prevLose(player, computer)[1] == True:
                board[prevLose(player, computer)[0]] = computer
                if checkWinner(player, computer, board):
                    printBoard(player, computer, playerChoice, computerChoice)
                    break  # Game ends if there's a winner
            elif tryWin(player, computer)[1] == False and prevLose(player, computer)[1] == False:
                board[tryMove(player, computer)[0]] = computer
                if checkWinner(player, computer, board):
                    printBoard(player, computer, playerChoice, computerChoice)
                    break  # Game ends if there's a winner
        printBoard(player, computer, playerChoice, computerChoice)
    else:
        print(colored("invalid , try a valid move","yellow"))
        printBoard(player, computer, playerChoice, computerChoice)
