arr = [["0" for i in range(7)] for j in range(6)]
turn = True

def checkHorizonal(arr, startR, coin):
    isThere = False
    for c in range(0, len(arr[startR])-3, 1):
        if arr[startR][c] == coin and arr[startR][c+1] == coin and arr[startR][c+2] == coin and arr[startR][c+3] == coin:
            isThere = True
            break
    return isThere
            

def checkVertical(arr, startC, coin):                                                                                                                                                                          
    isThere = False
    for r in range(len(arr)-1, 0, -1):
        if arr[r][startC] == coin and arr[r-1][startC] == coin and arr[r-2][startC] == coin and arr[r-3][startC] == coin:
            isThere = True
            break
    return isThere

def checkDiagonal(arr, coin):
    # Check positive diaganols
    for c in range(7-3):
        for r in range(6-3):
            if arr[r][c] == coin and arr[r+1][c+1] == coin and arr[r+2][c+2] == coin and arr[r+3][c+3] == coin:
                return True
 
    # Check negative diaganols
    for c in range(7-3):
        for r in range(3,6):
            if arr[r][c] == coin and arr[r-1][c+1] == coin and arr[r-2][c+2] == coin and arr[r-3][c+3] == coin:
                return True
            
def checkWin(arr, startR, startC, coin):
    return checkHorizonal(arr,startR,coin) or checkVertical(arr, startC, coin) or checkDiagonal(arr, coin)

def printBoard(arr):
    for row in arr:
        print(row)
            
def addCoin(col, arr, coin):
    for r in range(len(arr)-1, -1, -1):
        if arr[r][col] == "0":
            arr[r][col] = coin
            if(checkWin(arr, r, col, coin)):
                return True
            else:
                return False
                break
        
while True:
    if turn:
        if(addCoin(int(input("What colume do you want to place your piece (0-6): ")), arr, "R")):
            printBoard(arr)
            print("R WINS!!!!")
            break;
        else:
            printBoard(arr)
            turn = False
    else:
        if(addCoin(int(input("What colume do you want to place your piece (0-6): ")), arr, "Y")):
            printBoard(arr)
            print("Y WINS!!!!")
            break;
        else:
            printBoard(arr)
            turn = True

