from termcolor import colored

player, computer = None, None
board = list(range(1, 10))
wins=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
movesAlg=((1,3,7,9),(5,),(2,4,6,8))
def hasEmpty():
    return board.count("X") + board.count("O") != 9
def computerMove():
    compMove=-1
    for i in range(10):
        if makeMove(board,player,i,True)[1]:
            compMove=i
            break
    if compMove==-1:
        for j in range(1,10):
            if makeMove(board,computer,j,True)[1]:
                compMove=j
                break
    if compMove==-1:
        for tup in movesAlg:
            for m in tup:
                if compMove==-1 and validMove(board,m):
                    compMove=m
                    break
    return makeMove(board,computer,compMove)

def printBoard():
    j = 1
    for i in board:
        end = " "
        if j % 3 == 0:
            end = "\n"
        if i == player:
            print("\033[92m{}\033[0m".format(i), end=end)
        elif i == computer:
            print("\033[91m{}\033[0m".format(i), end=end)
        else:
            print("\033[97m{}\033[0m".format(i), end=end)
        j += 1

def makeMove(board, player,move,undo=False):
    if validMove(board,move):
        board[move-1] = player
        win = isWinner(board,player)
        if undo:
            board[move-1]=move
        return True,win
    return False,False
def isWinner(board,player):
    win=True
    for tup in wins:
        win=True
        for j in tup:
            if board[j]!=player:
                win=False
                break
        if win:
            break
    return win

def validMove(board,move):
    if move in range(1,10) and isinstance(board[move-1],int):
        return True
    else:
        return False
while True:
    selection = input("Select X or O: ")
    if "X" in selection or "x" in selection:
        player = "X"
        computer = "O"
        break
    elif "O" in selection or "o" in selection:
        player = "O"
        computer = "X"
        break
    else:
        print("Invalid, try again")

while hasEmpty():
    printBoard()
    move = int(input("Enter your move: (1-9) "))
    moved,win = makeMove(board,player,move)
    if not moved:
        print("Invalid, try again")
        continue
    if win:
        print("\033[92m{}\033[0m".format("you won"))
        break
    elif computerMove()[1]:
        print("\033[91m{}\033[0m".format("you lose"))
        break

printBoard()
