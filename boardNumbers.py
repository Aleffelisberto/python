import random
import subprocess

def createGameBoard():
    mat=[]
    numbers = list(range(0, 16))
    for i in range(4):
        arr = []
        for j in range(4):
            number = random.choice(numbers)
            numbers.remove(number)
            arr.append(str(number))
            if arr[j] == '0':
                arr[j] = ' '
        mat.append(arr)

    return mat

def showGameBoard(gameBoard):
    for i in range(4):
        for j in range(4):
            if j == 3:
                print(gameBoard[i][j], end="\n\n\n")
            else:
                print(gameBoard[i][j], end="\t")


def verifyMove(gameBoard, move, position):
    if move[1] not in ['l','r','u','d'] or int(move[0]) not in range(16):
        return False

    number = move[0]
    direction = move[1]
    index = [-1, -1]
    for i in range(4):
        if number in gameBoard[i]:
            idx = gameBoard[i].index(number)
            index[0] = i
            index[1] = idx
            break
        else:
            continue
    position.append(index[0])
    position.append(index[1])
    if direction == 'l':
        if (index[1] - 1) >= 0:
            if gameBoard[index[0]][index[1] - 1] == ' ':
                return True
            else: return False
    elif direction == 'r':
        if index[1] + 1 < 4:
            if gameBoard[index[0]][index[1] + 1] == ' ':
                return True
            else:
                return False
    elif direction == 'u':
        if index[0] - 1 >= 0:
            if gameBoard[index[0] - 1][index[1]] == ' ':
                return True
            else:
                return False
    else:
        if index[0] + 1 < 4:
            if gameBoard[index[0] + 1][index[1]] == ' ':
                return True
            else:
                return False

def winGame(gameBoard):
    if gameBoard == [['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15',' ']]:
        return True
    else:
        return False

def executeMove(gameBoard, move, idx): 
    direction = move[1]
    l = idx[0]
    c = idx[1]
    if direction == 'l':
        auxiliar = gameBoard[l][c]
        gameBoard[l][c] = gameBoard[l][c-1]
        gameBoard[l][c-1] = auxiliar
    elif direction == 'r':
        auxiliar = gameBoard[l][c]
        gameBoard[l][c] = gameBoard[l][c+1]
        gameBoard[l][c+1] = auxiliar
    elif direction == 'u':
        auxiliar = gameBoard[l][c]
        gameBoard[l][c] = gameBoard[l-1][c]
        gameBoard[l-1][c] = auxiliar 
    else:
        auxiliar = gameBoard[l][c]
        gameBoard[l][c] = gameBoard[l+1][c]
        gameBoard[l+1][c] = auxiliar


def clearScreen():
    subprocess.call("clear")

def main():
    gameBoard = createGameBoard() 
    stillPlaying = True
    while stillPlaying:
        clearScreen()
        index = list(()) 
        showGameBoard(gameBoard)
        if winGame(gameBoard):
            print("CONGRATULATIONS. YOU'VE FINISHED THE GAME!!")
            break

        ans = input("\n\ncontinue ? (Y, y - Yes/N, n - No): ")
        while True:
            clearScreen()
            showGameBoard(gameBoard)
            if ans == 'y' or ans == 'Y':
                move = tuple(input("\n\nEnter the number that you wanna move and the direction separated by a blankspace (l-left, r-right, u-up, d-down): ").split())
                while not verifyMove(gameBoard, move, index):
                    move = tuple(input("This move isn't allowed. Try a new move: ").split())
                print(move)
                executeMove(gameBoard, move, index)
                break
            elif ans == 'n' or ans == 'N':
                stillPlaying = False
                break
            else:
                ans = input("\n\nEnter a valid command. Continue ? (Y, y - Yes/N, n - No)")
            

if __name__ == '__main__':
    main()
    
