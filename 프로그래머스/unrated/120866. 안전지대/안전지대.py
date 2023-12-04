def solution(board):
    myboard = []
    for i in range(len(board) + 2):
        y = []
        for j in range(len(board[0]) + 2):
            y.append(0)
        myboard.append(y)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                myboard[i][j], myboard[i][j+1], myboard[i][j+2] = 1, 1, 1
                myboard[i+1][j], myboard[i+1][j+1], myboard[i+1][j+2] = 1, 1, 1
                myboard[i+2][j], myboard[i+2][j+1], myboard[i+2][j+2] = 1, 1, 1
    
    res = 0
    for i in range(1, len(myboard) - 1):
        for j in range(1, len(myboard[0]) - 1):
            res += myboard[i][j]
    
    return len(board) * len(board) - res 