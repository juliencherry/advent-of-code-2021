import sys

def parseInput():
    bingoDraws = []
    bingoBoards = []

    f = open('input.txt', 'r')
    for i, line in enumerate(f.readlines()):
        if i == 0:
            bingoDraws = line.split(',')
            continue
        elif i == 1:
            continue

        bingoBoardNumber = int((i - 2) / 6)
        bingoBoardRowNumber = (i - 2) % 6

        if bingoBoardRowNumber == 0:
            bingoBoards.append([line.split()])
        elif bingoBoardRowNumber < 5:
            bingoBoards[bingoBoardNumber].append(line.split())
    
    return bingoDraws, bingoBoards

def markBingoBoard(bingoBoard, numberDrawn):
    for i, row in enumerate(bingoBoard):
        for j, cell in enumerate(row):
            if cell == numberDrawn:
                bingoBoard[i][j] = numberDrawn + 'X'
                return bingoBoard

    return bingoBoard

def isWinner(bingoBoard):
    for row in range(0, 5):
        for column in range(0, 5):
            if not bingoBoard[row][column].endswith('X'):
                break 
            if column == 4:
                return True

    for column in range(0, 5):
        for row in range(0, 5):
            if not bingoBoard[row][column].endswith('X'):
                break 
            if row == 4:
                return True

    return False

def getLoser(bingoDraws, bingoBoards):
    for draw in bingoDraws:
        for i, board in enumerate(bingoBoards):
            bingoBoards[i] = markBingoBoard(board, draw)

        for i, board in enumerate(bingoBoards):
            if not isWinner(board):
                continue
            elif len(bingoBoards) == 1:
                return board, draw
                
            del bingoBoards[i]
        
def getScore(board, draw):
    score = 0
    for row in board:
        for cell in row:
            if not cell.endswith('X'):
                score += int(cell)
    
    score *= int(draw)
    return score
            
bingoDraws, bingoBoards = parseInput()
losingBoard, winningDraw = getLoser(bingoDraws, bingoBoards)
print(getScore(losingBoard, winningDraw))
